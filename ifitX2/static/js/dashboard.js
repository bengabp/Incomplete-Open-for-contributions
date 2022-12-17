let activityChart = document.getElementById("activity-per-day-chart");

var xValues = [0,1,2,3,4,5,6];
var yValues = [2,3,7,5,6,3,9];

let weekDays = ['Sun','Mon','Tue','Wed',"Thur",'Fri','Sat']

let activityiesPerDay = new Chart(activityChart, {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
        display:true,
        label:"Activities per day",
        backgroundColor: "#BFDBF7",
        data: [1,2,3,4,5,6,7],
    }]
  },
  options:{
    responsive:true,
    plugins:{
        legend:{
            display:false,
        },
        title:{
            display:true,
            text:"Activities",
            font:{
                size:20,
                family:'Signika',
                color:"#022B3A"
            }
        },
        subtitle:{
            display:true,
            text:"Your activities everyday",
            font:{
                size:16,
                family:"Signika"
            }
        }
    },
    
    scales:{
        x:{
            type:'linear',
            easing:'linear',
            ticks: {
                // Include a dollar sign in the ticks
                callback: function(value, index, ticks) {return weekDays[index];},
                font:{
                    color:'red'
                }
            },
            grid:{
                display:false
            },
            border:{
                display:false,
            }
        },
        y:{
            beginAtZero:true,
            ticks:{
                callback:(value,index,ticks) => ""
            },
            grid:{
                display:false
            },
            border:{
                display:false,
            }
            
        }
    },
  }
});