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
    const datasets = transformData(data, mode);
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

function main2(results, conf) {

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
        main2(results, conf);
    });
}

main();
