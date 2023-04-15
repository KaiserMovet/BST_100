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


function createPlot(element_id, title, mode) {
    fetch('results.json')
        .then(response => response.json())
        .then(data => {
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
                        }
                    }
                }
            });
            charts.push(lineChart);
        });
}

createPlot('addingChart', 'Adding elements to BST', "add");
createPlot('checkingChart', 'Checking elements in BST', "check");
createPlot('lenChart', 'Counting elements in BST', "len");
createPlot('heightChart', 'Counting height of BST', "height");

