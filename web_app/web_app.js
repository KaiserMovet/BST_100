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

class BSTTable {
    constructor(results) {
        this.element = document.getElementById("bstTable");
        this.cells = {};
        this.results = results;
        this.createDropdownMenu();
        this.createTable(results);

        // Call refreshData with the value of the last option.
        this.refreshData(this.results.amounts[this.results.amounts.length - 1]);
    }

    createDropdownMenu() {
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

        this.element.appendChild(select);
    }

    refreshData(amount) {
        this.results.languages.forEach((lang) => {
            this.results.tests.forEach((test) => {
                const value = this.results.data[lang][amount][test];
                console.log(this.cells)
                this.cells[lang][test].textContent = formatNumber(value)
            })
        })
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
}

function main2(results, conf) {

    new BSTTable(results)
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
