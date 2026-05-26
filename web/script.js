/**
 * Simple frontend for SQL to NoSQL transpiler.
 */

const sqlInput = document.getElementById('sql-input');
const convertBtn = document.getElementById('convert-btn');
const clearBtn = document.getElementById('clear-btn');
const exampleBtn = document.getElementById('example-btn');
const targetDbSelect = document.getElementById('target-db');
const resultsSection = document.getElementById('results');
const loadingSection = document.getElementById('loading');
const errorSection = document.getElementById('error');
const errorMessage = document.getElementById('error-message');

const tabButtons = document.querySelectorAll('.tab');
const tabPanels = document.querySelectorAll('.tab-panel');

const astOutput = document.getElementById('ast-output');
const uastOutput = document.getElementById('uast-output');
const targetOutput = document.getElementById('target-output');

const targetTabNameEl = document.getElementById('target-tab-name');
const targetQueryTitleEl = document.getElementById('target-query-title');

const targetConfigs = {
    mongodb: { name: 'MongoDB' },
    cassandra: { name: 'Cassandra' },
    dynamodb: { name: 'DynamoDB' },
    redis: { name: 'Redis' },
};

const exampleQueries = [
    'SELECT name, age FROM users WHERE age > 25 LIMIT 10',
    'SELECT * FROM products WHERE price < 100',
    'SELECT title, author FROM books WHERE rating >= 4.5 LIMIT 5',
    "SELECT email FROM customers WHERE status = 'active'",
    'SELECT * FROM logs ORDER BY timestamp DESC LIMIT 100',
];

let currentExampleIndex = 0;

function updateTargetLabels() {
    const id = targetDbSelect.value;
    const label = targetConfigs[id]?.name || id;
    const nameEl = document.getElementById('target-name');
    if (nameEl) nameEl.textContent = label;
    if (targetTabNameEl) targetTabNameEl.textContent = label;
    if (targetQueryTitleEl) targetQueryTitleEl.textContent = label;
}

targetDbSelect.addEventListener('change', updateTargetLabels);
convertBtn.addEventListener('click', convertSQL);
clearBtn.addEventListener('click', clearInput);
exampleBtn.addEventListener('click', loadExample);

tabButtons.forEach((button) => {
    button.addEventListener('click', () => switchTab(button.dataset.tab));
});

document.querySelectorAll('.copy-btn').forEach((button) => {
    button.addEventListener('click', () => copyToClipboard(button));
});

sqlInput.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        e.preventDefault();
        convertSQL();
    }
    if (e.ctrlKey && e.key === 'l') {
        e.preventDefault();
        clearInput();
    }
});

async function convertSQL() {
    const sqlQuery = sqlInput.value.trim();
    const target = targetDbSelect.value;

    if (!sqlQuery) {
        showError('Please enter a SQL query.');
        return;
    }

    showLoading();
    hideError();
    hideResults();

    try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 15000);

        const response = await fetch('/convert', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sql: sqlQuery, target }),
            signal: controller.signal,
        });

        clearTimeout(timeoutId);
        const data = await response.json();

        if (!response.ok || data.error) {
            throw new Error(data.error || `HTTP ${response.status}`);
        }

        if (data.platform) {
            if (targetTabNameEl) targetTabNameEl.textContent = data.platform;
            if (targetQueryTitleEl) targetQueryTitleEl.textContent = data.platform;
        }

        displayResults(data);
    } catch (error) {
        if (error.name === 'AbortError') {
            showError('Request timed out. Please try again.');
        } else {
            showError(error.message || 'Conversion failed.');
        }
    } finally {
        hideLoading();
    }
}

function displayResults(data) {
    astOutput.textContent = data.ast || '';
    uastOutput.textContent = data.uast || '';
    targetOutput.textContent = data.target || '';
    resultsSection.style.display = 'block';
    switchTab('target');
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function switchTab(tabName) {
    tabButtons.forEach((btn) => {
        btn.classList.toggle('active', btn.dataset.tab === tabName);
    });
    tabPanels.forEach((panel) => {
        panel.classList.toggle('active', panel.id === `${tabName}-tab`);
    });
}

async function copyToClipboard(button) {
    const targetId = button.dataset.target;
    const text = document.getElementById(targetId).textContent;

    try {
        await navigator.clipboard.writeText(text);
        button.textContent = 'Copied';
        button.classList.add('copied');
        setTimeout(() => {
            button.textContent = 'Copy';
            button.classList.remove('copied');
        }, 2000);
    } catch {
        alert('Could not copy to clipboard.');
    }
}

function clearInput() {
    sqlInput.value = '';
    sqlInput.focus();
    hideResults();
    hideError();
}

function downloadAll() {
    const label = targetConfigs[targetDbSelect.value]?.name || targetDbSelect.value;
    const content =
        `SQL to NoSQL Results\n` +
        `Generated: ${new Date().toLocaleString()}\n` +
        `Target: ${label}\n\n` +
        `SQL:\n${sqlInput.value}\n\n` +
        `AST:\n${astOutput.textContent}\n\n` +
        `UAST:\n${uastOutput.textContent}\n\n` +
        `${label}:\n${targetOutput.textContent}\n`;

    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `sql-to-${targetDbSelect.value}.txt`;
    a.click();
    URL.revokeObjectURL(url);
}

function dismissError() {
    hideError();
}

function loadExample() {
    sqlInput.value = exampleQueries[currentExampleIndex];
    currentExampleIndex = (currentExampleIndex + 1) % exampleQueries.length;
    sqlInput.focus();
}

function setExample(sqlQuery) {
    sqlInput.value = sqlQuery;
    sqlInput.focus();
}

function showLoading() {
    loadingSection.style.display = 'block';
    convertBtn.disabled = true;
    convertBtn.textContent = 'Converting…';
}

function hideLoading() {
    loadingSection.style.display = 'none';
    convertBtn.disabled = false;
    const label = targetConfigs[targetDbSelect.value]?.name || 'MongoDB';
    convertBtn.innerHTML = `Convert to <span id="target-name">${label}</span>`;
}

function showError(message) {
    errorMessage.textContent = message;
    errorSection.style.display = 'block';
}

function hideError() {
    errorSection.style.display = 'none';
}

function hideResults() {
    resultsSection.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    updateTargetLabels();
    sqlInput.focus();
});
