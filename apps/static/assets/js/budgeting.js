var monthly_total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

$(document).ready(function() {
    $.ajax({
        url: 'grocery_history',
        type: 'POST',
        success: function(data) {
            if (data.type == "nosql") {
                purchases = data.purchases

                var purchases = [...new Map(purchases.map(item => [JSON.stringify(item), item])).values()];
                purchases.forEach(element => {
                    var date = new Date(element["date"]);
                    element["date"] = date.getMonth() + 1;
                    console.log(element["date"]);
                });

                var sorted_purchases = purchases.reduce(function(r, a) {
                    r[a.date] = r[a.date] || [];
                    r[a.date].push(a);
                    return r;
                }, Object.create(null));

                for (const [key, value] of Object.entries(sorted_purchases)) {
                    console.log(value);
                    for (var i = 0; i < Object.keys(value).length; i++) {
                        monthly_total[key - 1] += value[i]["total_amount"];
                    }
                }
            } else {
                data = data.purchases

                for (const item in data) {
                    monthly_total[item - 1] = getSum(data[item])
                }
            }
            initialiseChart(monthly_total);
        }
    });
});

function getSum(array) {
    var sum = array.reduce(function(a, b) {
        return a + b;
    }, 0);
    return sum;
}

function initialiseChart(monthly_total) {
    const ctx = document.getElementById('myChart');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [{
                label: '$ Amount Spent',
                data: monthly_total,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}