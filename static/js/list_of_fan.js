window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer", {
		title:{
			text: "Music Data API : List of Fans"              
		},
		data: [              
		{
			// Change type to "doughnut", "line", "splineArea", etc.
			type: "column",
			dataPoints: [
				{ label: "Blackpink",  y: 100  },
				{ label: "Justin Bieber", y: 15  },
				{ label: "IZ*ONE", y: 25  },
				{ label: "SNSD",  y: 30  },
				{ label: "Tobu",  y: 28  }
			]
		}
		]
	});
	chart.render();

}