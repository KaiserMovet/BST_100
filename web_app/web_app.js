class Results {
    constructor(result) {
        this.data = result;
    }

    get languages() {
        return Object.keys(this.data)
    }

    get amounts() {
        var language = Object.keys(this.data)[0]
        return Object.keys(this.data[language])
    }

    get tests() {
        var language = this.languages[0]
        var amount = this.amounts[0]
        return Object.keys(this.data[language][amount])
    }

    getDataForAmountForBstChart(amount) {
        var full_data = [];
        this.tests.forEach(test => {
            var data = {};
            data['label'] = test
            data['data'] = []
            this.languages.forEach(lang => {
                data['data'].push({ y: lang, x: this.data[lang][amount][test] });
            })
            full_data.push(data)
        })

        return full_data
    }


}

function transformData(data, mode) {
    return Object.keys(data).map(langKey => ({
        label: langKey,
        cubicInterpolationMode: 'monotone',
        data: Object.keys(data[langKey]).map(amountKey => ({
            x: Number(amountKey),
            y: Number(data[langKey][amountKey][mode])
        })).sort((a, b) => a.x - b.x)
    }));
}

let charts = [];


function createPlot(data, element_id, title, mode) {

    const ctx = document.getElementById(element_id).getContext('2d');
    const datasets = transformData(data.data, mode);
    const lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: datasets
        },
        options: {
            plugins: {
                legend: {
                    onClick: function (e, legendItem) {
                        const index = legendItem.datasetIndex;
                        const ci = this.chart;

                        // Toggle the visibility of this dataset
                        ci.getDatasetMeta(index).hidden = ci.isDatasetVisible(index) ? true : false;

                        // Now loop over the other charts and do the same
                        charts.forEach((chart) => {
                            if (chart !== ci) {
                                const otherMeta = chart.getDatasetMeta(index);
                                otherMeta.hidden = ci.getDatasetMeta(index).hidden;
                                chart.update();
                            }
                        });
                        ci.update();
                    },
                },
                title: {
                    display: true,
                    text: title,
                },
            },
            interaction: {
                intersect: false,
                mode: 'index',
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Amount of elements'
                    },
                    beginAtZero: true,
                    type: 'linear',
                },
                y: {
                    title: {
                        display: true,
                        text: "Time (s)",
                    },
                    beginAtZero: true,
                    type: 'linear',
                }
            }
        }
    });
    charts.push(lineChart);
}

function formatNumber(num) {
    if (typeof num !== 'number') {
        return num;
    }
    if (num > 1e3) {
        return num.toFixed(0);
    } else if (num > 1e1) {
        return num.toFixed(2);
    } else if (num < 1e-4) {
        return num.toExponential(4);
    } else {
        return num.toFixed(4);
    }
}

class BSTConfig {
    constructor(conf, start_lang) {
        this.conf = conf;
        this.element = document.getElementById("configBox");
        this.table = document.createElement('table');
        this.element.appendChild(this.table);
        this.setConfig(start_lang)
    }

    clear() {
        // Clear the table
        this.table.innerHTML = '';
    }

    setConfig(language) {
        this.clear();
        var config = this.conf[language]
        // Add language row
        let tr = document.createElement('tr');
        let th = document.createElement('th');
        th.textContent = "Language";
        tr.appendChild(th);
        let td = document.createElement('td');
        td.textContent = language;
        tr.appendChild(td);
        this.table.appendChild(tr);

        // Add config rows
        for (let key in config) {
            if (key == "language") continue;
            tr = document.createElement('tr');
            th = document.createElement('th');
            th.textContent = key;
            tr.appendChild(th);
            td = document.createElement('td');
            td.textContent = config[key];
            tr.appendChild(td);
            this.table.appendChild(tr);
        }
    }
}

class BSTTable {
    constructor(results, box_config, bst_chart) {
        this.element = document.getElementById("bstTable");
        this.box_config = box_config;
        this.bst_chart = bst_chart;
        this.cells = {};
        this.results = results;
        this.createDropdownMenu();
        this.createTable(results);

        // Call refreshData with the value of the last option.
        this.refreshData(this.results.amounts[this.results.amounts.length - 1]);
    }

    createDropdownMenu() {
        const container = document.createElement('div');
        container.className = 'dropdown-container';
        this.element.appendChild(container);

        const label = document.createElement('label');
        label.textContent = "For ";
        container.appendChild(label);

        const select = document.createElement('select');
        this.results.amounts.forEach(amount => {
            const option = document.createElement('option');
            option.textContent = amount;
            option.value = amount;
            select.appendChild(option);
        });

        // Set the selected option to the last element.
        select.selectedIndex = this.results.amounts.length - 1;

        select.addEventListener('change', (event) => {
            this.refreshData(event.target.value);
        });

        container.appendChild(select);
    }

    refreshData(amount) {
        this.current_amount = amount;
        this.results.languages.forEach((lang) => {
            this.results.tests.forEach((test) => {
                const value = this.results.data[lang][amount][test];
                console.log(this.cells)
                this.cells[lang][test].textContent = formatNumber(value)
            })
        })
        this.bst_chart.updateData(amount, "add");
    }

    createTable(results) {
        var table = document.createElement('table');
        table.appendChild(this.createHeader(results))
        this.element.appendChild(table);
        var rows = this.createRows(results);
        rows.forEach(row => {
            table.appendChild(row)
        })
    }
    createHeader(results) {
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        const langHeader = document.createElement('th');
        langHeader.textContent = "Language";
        headerRow.appendChild(langHeader);
        results.tests.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        return thead;
    }

    createRow(language, results) {
        const row = document.createElement('tr');

        // Add event listener for click
        row.addEventListener('mouseover', () => {
            this.onHover(language);
        });

        row.addEventListener('mouseout', () => {
            this.exitHover(language);
        });

        row.addEventListener('click', () => {
            // Remove 'clicked' class from all rows
            Array.from(this.element.getElementsByTagName('tr')).forEach((otherRow) => {
                otherRow.classList.remove('clicked');
            });

            // Add 'clicked' class to the clicked row
            row.classList.add('clicked');

            this.onClick(language);
        });

        // Name
        const langCell = document.createElement('td');
        langCell.textContent = language;
        row.appendChild(langCell);
        this.cells[language] = {};
        results.tests.forEach(test => {
            var cell = document.createElement('td');
            this.cells[language][test] = cell
            row.appendChild(cell);
        })

        return row
    }

    createRows(results) {
        var rows = [];
        results.languages.forEach(lang => {
            rows.push(this.createRow(lang, results));
        })

        return rows;
    }

    onClick(language) {
        console.log('onClick', language);
    }
    onHover(language) {
        this.box_config.setConfig(language, {});
    }

    exitHover(language) {
        // this.box_config.clear();
    }
}

class BSTChart {
    constructor(results) {
        this.results = results;
        const ctx = document.getElementById("bstChartCan").getContext('2d');
        this.chart = new Chart(ctx, {
            type: 'bar',
            data: {
                datasets: []
            },
            options: {
                maintainAspectRatio: false,
                indexAxis: 'y',
                scales: {
                    x: {
                        title: {
                            display: false,
                            text: 'Time (s)'
                        },
                        beginAtZero: true,
                        type: 'logarithmic',
                    },

                }
            },

        });
    }

    updateData(amount, test) {
        this.chart.data.datasets = this.results.getDataForAmountForBstChart(amount)
        this.chart.update();
    }
}


function main2(results, conf) {
    const box_config = new BSTConfig(conf, results.languages[0]);
    const bst_chart = new BSTChart(results);
    new BSTTable(results, box_config, bst_chart)
    createPlot(results, 'addingChart', 'Adding elements to BST', "add");
    createPlot(results, 'checkingChart', 'Checking elements in BST', "check");
    createPlot(results, 'lenChart', 'Counting elements in BST', "len");
    createPlot(results, 'heightChart', 'Counting height of BST', "height");
}

function main() {
    Promise.all([
        fetch('results/results.json').then(response => response.json()),
        fetch('results/conf.json').then(response => response.json())
    ]).then(([results, conf]) => {
        main2(new Results(results), conf);
    });
}

main();
