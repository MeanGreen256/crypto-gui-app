import React from 'react';
import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale,
} from 'chart.js';
import 'chartjs-adapter-date-fns';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
);

const PriceChart = ({ chartData, days }) => {
  const data = {
    labels: chartData.prices.map((price) => new Date(price[0])),
    datasets: [
      {
        label: 'Bitcoin Price (USD)',
        data: chartData.prices.map((price) => price[1]),
        borderColor: '#61dafb',
        backgroundColor: 'rgba(97, 218, 251, 0.2)',
        tension: 0.1,
        pointRadius: 0, // Hide points for a cleaner look
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: `Bitcoin Price (Last ${days} Days)`,
      },
    },
    scales: {
      x: {
        type: 'time',
        time: { unit: 'day' },
        grid: { display: false }
      },
    },
  };

  return <Line options={options} data={data} />;
};

export default PriceChart;

