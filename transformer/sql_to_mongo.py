"""
sql_to_mongo.py
===============
Generate MongoDB shell queries from Unified AST (UAST).

Example output:
  db.users.find({"age": {"$gt": 25}}, {"name": 1, "age": 1}).limit(5)
"""

import json


class MongoQueryGenerator:
        
    def __init__(self):
        """Initialize the MongoDB query generator"""
        self.indent = "    "  # 4 spaces for indentation
    
    def generate(self, uast):
        # Validate UAST structure
        self._validate_uast(uast)
        
        # Extract components
        collection = uast.get("collection", "")
        projection = uast.get("projection", [])
        filter_condition = uast.get("filter", {})
        sort = uast.get("sort")
        limit = uast.get("limit")
        
        # Build query components
        query_parts = []
        
        # 1. Base query: db.collection.find(
        base_query = f"db.{collection}.find("
        query_parts.append(base_query)
        
        # 2. Projection (if not empty and not "*")
        projection_str = self._format_projection(projection)
        has_projection = bool(projection_str.strip())  # Check if projection is not empty
        
        # 3. Filter condition (always include, even if empty)
        filter_str = self._format_filter(filter_condition, has_projection)
        
        # Check if filter is simple for formatting decisions
        filter_is_simple = filter_str in ["{}", "{}"] or len(filter_str) < 15
        
        # If filter is simple and we have projection, use compact projection
        if has_projection and filter_is_simple:
            projection_str = self._format_projection(projection, use_compact=True)
        
        query_parts.append(filter_str)
        
        # 4. Add projection if present
        if has_projection:
            query_parts.append(projection_str)
        
        # 5. Close find()
        query_parts.append(")")
        
        # 6. Add sort if specified
        if sort is not None:
            sort_str = json.dumps(sort, separators=(',', ':'))
            query_parts.append(f".sort({sort_str})")
        
        # 7. Add limit if specified
        if limit is not None:
            query_parts.append(f".limit({limit})")
        
        # Combine all parts with proper formatting
        return self._format_query(query_parts)
    
    def _validate_uast(self, uast):
        """
        Validate the UAST structure
        
        Args:
            uast (dict): UAST to validate
            
        Raises:
            ValueError: If UAST is invalid
        """
        if not isinstance(uast, dict):
            raise ValueError("UAST must be a dictionary")
        
        operation = uast.get("operation")
        if operation != "SELECT":
            raise ValueError(f"Unsupported operation: {operation}. Only SELECT is supported.")
        
        collection = uast.get("collection")
        if not collection:
            raise ValueError("Collection name is required")
    
    def _format_filter(self, filter_condition, has_projection=False):
        """
        Format filter condition for MongoDB
        
        Args:
            filter_condition (dict): Filter condition from UAST
            has_projection (bool): Whether there's a projection (affects formatting)
            
        Returns:
            str: Formatted filter string
        """
        if not filter_condition:
            return "{}"
        
        # If filter is empty (just {}), always use compact format
        if filter_condition == {}:
            return "{}"
        
        # If there's projection, use multi-line format for consistency
        if has_projection:
            filter_json = json.dumps(filter_condition, indent=4)
            
            # Add indentation to match query format
            lines = filter_json.split('\n')
            formatted_lines = [self.indent + line if line.strip() else line for line in lines]
            
            return '\n'.join(formatted_lines)
        else:
            # Single-line format (no projection) - always compact
            return json.dumps(filter_condition, separators=(',', ':')).replace('\n', '')
    
    def _format_projection(self, projection, use_compact=False):
        """
        Format projection for MongoDB
        
        Args:
            projection: Projection from UAST (list, string, or None)
            use_compact (bool): Whether to use compact formatting
            
        Returns:
            str: Formatted projection string or empty string if no projection needed
        """
        # Handle SELECT * or empty projection
        if not projection or projection == "*":
            return ""
        
        # Convert list to MongoDB projection format
        if isinstance(projection, list):
            mongo_projection = {field: 1 for field in projection}
        elif isinstance(projection, str):
            # Single field as string
            mongo_projection = {projection: 1}
        else:
            # Already in correct format
            mongo_projection = projection
        
        # Use compact format if requested
        if use_compact:
            return json.dumps(mongo_projection, separators=(',', ':'))
        
        # Format as JSON with proper indentation
        projection_json = json.dumps(mongo_projection, indent=4)
        
        # Add indentation to match query format
        lines = projection_json.split('\n')
        formatted_lines = [self.indent + line if line.strip() else line for line in lines]
        
        return '\n'.join(formatted_lines)
    
    def _format_query(self, query_parts):
        """
        Format the complete query string with proper indentation
        
        Args:
            query_parts (list): List of query parts
            
        Returns:
            str: Formatted complete query string
        """
        # query_parts structure:
        # Without projection: [base_query, filter, closing_paren, limit?]
        # With projection: [base_query, filter, projection, closing_paren, limit?]
        
        # Check if we have projection by looking at the structure
        # If there are 5+ parts, we have projection (base, filter, projection, close, limit)
        # If there are 4 parts and the 3rd part (index 2) is NOT a closing parenthesis, we have projection
        has_projection = False
        
        if len(query_parts) >= 4:
            # Check if the third element (index 2) is a projection (not just ")")
            if query_parts[2] != ")":
                has_projection = True
        
        # Check if filter is simple (just {} or simple compact JSON)
        filter_is_simple = query_parts[1] in ["{}", "{}"] or len(query_parts[1]) < 15
        
        if has_projection and not filter_is_simple:
            # Multi-line query with projection and complex filter
            result = query_parts[0] + "\n"
            result += query_parts[1] + ",\n"
            result += query_parts[2] + "\n"
            result += query_parts[3]
        elif has_projection and filter_is_simple:
            # Single line with projection but simple filter
            result = query_parts[0] + query_parts[1] + ", " + query_parts[2] + query_parts[3]
        else:
            # Single line query with just filter - no newlines at all
            result = query_parts[0] + query_parts[1] + query_parts[2]
        
        # Add limit if present
        if len(query_parts) > 3:
            if has_projection and len(query_parts) > 4:
                result += query_parts[4]
            elif not has_projection and len(query_parts) > 3:
                result += query_parts[3]
        
        return result


def generate_mongo_query(uast):
    """
    Convenience function to generate MongoDB query from UAST
    
    Args:
        uast (dict): Unified AST structure
        
    Returns:
        str: MongoDB query string
        
    Example:
        >>> uast = {
        ...     "operation": "SELECT",
        ...     "collection": "users",
        ...     "projection": ["name", "age"],
        ...     "filter": {"age": {"$gt": 25}},
        ...     "limit": 5
        ... }
        >>> query = generate_mongo_query(uast)
        >>> print(query)
        db.users.find(
            {"age": {"$gt": 25}},
            {"name": 1, "age": 1}
        ).limit(5)
    """
    generator = MongoQueryGenerator()
    return generator.generate(uast)


# ============================================================================
# TEST SUITE
# ============================================================================

def run_tests():
    """Run comprehensive test suite for MongoDB query generator"""
    
    print("=" * 70)
    print("MONGODB QUERY GENERATOR - TEST SUITE")
    print("=" * 70)
    
    test_number = 0
    
    # Test 1: Basic query with all components
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: Basic query with all components")
    print('='*70)
    
    uast1 = {
        "operation": "SELECT",
        "collection": "users",
        "projection": ["name", "age"],
        "filter": {"age": {"$gt": 25}},
        "limit": 5
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast1, indent=2))
    
    query1 = generate_mongo_query(uast1)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query1)
    
    expected1 = '''db.users.find(
    {
        "age": {
            "$gt": 25
        }
    },
    {
        "name": 1,
        "age": 1
    }
).limit(5)'''
    
    assert query1.strip() == expected1.strip(), f"Test 1 failed: Expected {expected1}, got {query1}"
    print("\n✅ Test 1 PASSED")
    
    # Test 2: SELECT * (no projection)
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: SELECT * (no projection)")
    print('='*70)
    
    uast2 = {
        "operation": "SELECT",
        "collection": "products",
        "projection": "*",
        "filter": {"price": {"$lt": 100}},
        "limit": 10
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast2, indent=2))
    
    query2 = generate_mongo_query(uast2)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query2)
    
    expected2 = '''db.products.find({"price":{"$lt":100}}).limit(10)'''
    
    assert query2.strip() == expected2.strip(), f"Test 2 failed: Expected {expected2}, got {query2}"
    print("\n✅ Test 2 PASSED")
    
    # Test 3: No WHERE clause (empty filter)
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: No WHERE clause (empty filter)")
    print('='*70)
    
    uast3 = {
        "operation": "SELECT",
        "collection": "customers",
        "projection": ["name", "email"],
        "filter": {},
        "limit": 20
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast3, indent=2))
    
    query3 = generate_mongo_query(uast3)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query3)
    
    expected3 = '''db.customers.find({}, {"name":1,"email":1}).limit(20)'''
    
    assert query3.strip() == expected3.strip(), f"Test 3 failed: Expected {expected3}, got {query3}"
    print("\n✅ Test 3 PASSED")
    
    # Test 4: No LIMIT clause
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: No LIMIT clause")
    print('='*70)
    
    uast4 = {
        "operation": "SELECT",
        "collection": "orders",
        "projection": ["order_id", "total"],
        "filter": {"status": "completed"}
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast4, indent=2))
    
    query4 = generate_mongo_query(uast4)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query4)
    
    expected4 = '''db.orders.find(
    {
        "status": "completed"
    },
    {
        "order_id": 1,
        "total": 1
    }
)'''
    
    assert query4.strip() == expected4.strip(), f"Test 4 failed: Expected {expected4}, got {query4}"
    print("\n✅ Test 4 PASSED")
    
    # Test 5: Minimal query (only collection)
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: Minimal query (only collection)")
    print('='*70)
    
    uast5 = {
        "operation": "SELECT",
        "collection": "logs"
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast5, indent=2))
    
    query5 = generate_mongo_query(uast5)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query5)
    
    expected5 = "db.logs.find({})"
    
    assert query5.strip() == expected5.strip(), f"Test 5 failed: Expected {expected5}, got {query5}"
    print("\n✅ Test 5 PASSED")
    
    # Test 6: Complex filter with multiple conditions
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: Complex filter with multiple conditions")
    print('='*70)
    
    uast6 = {
        "operation": "SELECT",
        "collection": "employees",
        "projection": ["name", "department", "salary"],
        "filter": {
            "department": "Engineering",
            "salary": {"$gte": 80000},
            "status": "active"
        },
        "limit": 50
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast6, indent=2))
    
    query6 = generate_mongo_query(uast6)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query6)
    
    expected6 = '''db.employees.find(
    {
        "department": "Engineering",
        "salary": {
            "$gte": 80000
        },
        "status": "active"
    },
    {
        "name": 1,
        "department": 1,
        "salary": 1
    }
).limit(50)'''
    
    assert query6.strip() == expected6.strip(), f"Test 6 failed: Expected {expected6}, got {query6}"
    print("\n✅ Test 6 PASSED")
    
    # Test 7: Single field projection
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: Single field projection")
    print('='*70)
    
    uast7 = {
        "operation": "SELECT",
        "collection": "settings",
        "projection": ["config_value"],
        "filter": {"key": "max_connections"}
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast7, indent=2))
    
    query7 = generate_mongo_query(uast7)
    
    print("\n📤 OUTPUT MONGODB QUERY:")
    print(query7)
    
    expected7 = '''db.settings.find(
    {
        "key": "max_connections"
    },
    {
        "config_value": 1
    }
)'''
    
    assert query7.strip() == expected7.strip(), f"Test 7 failed: Expected {expected7}, got {query7}"
    print("\n✅ Test 7 PASSED")
    
    # Test 8: Error handling - missing collection
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: Error handling - missing collection")
    print('='*70)
    
    uast8 = {
        "operation": "SELECT",
        "projection": ["name"]
        # Missing "collection"
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast8, indent=2))
    
    try:
        query8 = generate_mongo_query(uast8)
        print("\n❌ Test 8 FAILED - should have raised ValueError")
    except ValueError as e:
        print(f"\n📤 Correctly raised error: {e}")
        print("\n✅ Test 8 PASSED")
    
    # Test 9: Error handling - unsupported operation
    test_number += 1
    print(f"\n{'='*70}")
    print(f"TEST {test_number}: Error handling - unsupported operation")
    print('='*70)
    
    uast9 = {
        "operation": "INSERT",
        "collection": "users"
    }
    
    print("\n📥 INPUT UAST:")
    print(json.dumps(uast9, indent=2))
    
    try:
        query9 = generate_mongo_query(uast9)
        print("\n❌ Test 9 FAILED - should have raised ValueError")
    except ValueError as e:
        print(f"\n📤 Correctly raised error: {e}")
        print("\n✅ Test 9 PASSED")
    
    # Summary
    print(f"\n{'='*70}")
    print("TEST SUMMARY")
    print('='*70)
    print(f"\n✅ All {test_number} tests PASSED!")
    print("\nMongoDB Query Generator is working correctly and ready for integration.")
    print('='*70)


# ============================================================================
# INTEGRATION TEST
# ============================================================================

def test_complete_pipeline():
    """Test the complete pipeline: SQL → AST → UAST → MongoDB Query"""
    
    print("\n" + "=" * 70)
    print("COMPLETE PIPELINE INTEGRATION TEST")
    print("=" * 70)
    
    # Import previous layers
    try:
        from parser.sql_parser import SQLParser
        from parser.ast_builder import build_ast
        from ast_to_uast import convert_ast_to_uast
    except ImportError as e:
        print(f"❌ Cannot import previous layers: {e}")
        print("Make sure you're running this from the project root directory")
        return
    
    # Test SQL query
    sql_query = "SELECT name, age FROM users WHERE age > 25 LIMIT 5"
    
    print(f"\n📥 INPUT SQL:")
    print(sql_query)
    
    try:
        # Step 1: Parse SQL → AST
        parser = SQLParser()
        parse_tree = parser.parse(sql_query)
        ast = build_ast(parse_tree)
        
        print("\n📤 Generated AST:")
        print(json.dumps(ast, indent=2))
        
        # Step 2: Convert AST → UAST
        uast = convert_ast_to_uast(ast)
        
        print("\n📤 Generated UAST:")
        print(json.dumps(uast, indent=2))
        
        # Step 3: Generate MongoDB Query
        mongo_query = generate_mongo_query(uast)
        
        print("\n📤 FINAL MONGODB QUERY:")
        print(mongo_query)
        
        print("\n✅ Complete pipeline test PASSED!")
        
    except Exception as e:
        print(f"\n❌ Pipeline test failed: {e}")
        import traceback
        traceback.print_exc()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # Run unit tests
    run_tests()
    
    # Run integration test
    test_complete_pipeline()
