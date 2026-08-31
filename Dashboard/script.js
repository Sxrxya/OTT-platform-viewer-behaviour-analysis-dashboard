// Common Chart Settings
Chart.defaults.color = '#C5C6C7';
Chart.defaults.font.family = "'Outfit', sans-serif";
Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(31, 40, 51, 0.9)';
Chart.defaults.plugins.tooltip.padding = 10;
Chart.defaults.plugins.tooltip.cornerRadius = 8;

const gridColor = 'rgba(255, 255, 255, 0.05)';

// 1. Churn vs Engagement Chart
const ctxChurn = document.getElementById('churnEngagementChart').getContext('2d');
new Chart(ctxChurn, {
    type: 'bar',
    data: {
        labels: ['< 5 hrs', '5-15 hrs', '15-30 hrs', '30-50 hrs', '50+ hrs'],
        datasets: [{
            label: 'Churn Rate (%)',
            data: [35, 28, 12, 5, 2],
            backgroundColor: [
                'rgba(229, 9, 20, 0.8)', // Red for high churn
                'rgba(229, 9, 20, 0.6)',
                'rgba(58, 134, 255, 0.5)',
                'rgba(56, 176, 0, 0.5)',
                'rgba(56, 176, 0, 0.8)' // Green for low churn
            ],
            borderRadius: 6
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { display: false }
        },
        scales: {
            y: { grid: { color: gridColor }, beginAtZero: true },
            x: { grid: { display: false } }
        }
    }
});

// 2. Viewer Preferences by Device
const ctxDevice = document.getElementById('deviceChart').getContext('2d');
new Chart(ctxDevice, {
    type: 'doughnut',
    data: {
        labels: ['Smart TV (44%)', 'Mobile (30%)', 'Desktop (16%)', 'Tablet (10%)'],
        datasets: [{
            data: [44, 30, 16, 10],
            backgroundColor: [
                '#3A86FF', // Blue
                '#8338EC', // Purple
                '#FFBE0B', // Yellow
                '#FF006E'  // Pink
            ],
            borderWidth: 0,
            hoverOffset: 4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: 'right' }
        },
        cutout: '70%'
    }
});

// 3. Subscription Tier Retention
const ctxTier = document.getElementById('tierChart').getContext('2d');
new Chart(ctxTier, {
    type: 'pie',
    data: {
        labels: ['Premium (89.5% Retained)', 'Standard (70% Retained)', 'Basic (55% Retained)'],
        datasets: [{
            data: [89.5, 70, 55], // retention rates
            backgroundColor: [
                '#38B000', // Green
                '#3A86FF', // Blue
                '#E50914'  // Red
            ],
            borderWidth: 0,
            hoverOffset: 4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: 'bottom' }
        }
    }
});

// 4. Top Genres
const ctxGenre = document.getElementById('genreChart').getContext('2d');
new Chart(ctxGenre, {
    type: 'polarArea',
    data: {
        labels: ['Action', 'Sci-Fi', 'Drama', 'Documentary', 'Comedy', 'Romance'],
        datasets: [{
            data: [25, 20, 18, 15, 12, 10],
            backgroundColor: [
                'rgba(255, 0, 110, 0.6)',
                'rgba(131, 56, 236, 0.6)',
                'rgba(58, 134, 255, 0.6)',
                'rgba(56, 176, 0, 0.6)',
                'rgba(255, 190, 11, 0.6)',
                'rgba(251, 86, 7, 0.6)'
            ],
            borderWidth: 1,
            borderColor: '#1F2833'
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: 'right' }
        },
        scales: {
            r: {
                grid: { color: gridColor },
                ticks: { display: false }
            }
        }
    }
});

// 5. Peak Streaming Times
const ctxTime = document.getElementById('timeChart').getContext('2d');
new Chart(ctxTime, {
    type: 'line',
    data: {
        labels: ['6 AM', '9 AM', '12 PM', '3 PM', '6 PM', '8 PM', '10 PM', '12 AM'],
        datasets: [{
            label: 'Active Users',
            data: [500, 1200, 2500, 2000, 6000, 14000, 16000, 8000],
            borderColor: '#66FCF1',
            backgroundColor: 'rgba(102, 252, 241, 0.1)',
            borderWidth: 3,
            fill: true,
            tension: 0.4 // smooth curve
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { display: false }
        },
        scales: {
            y: { grid: { color: gridColor }, beginAtZero: true },
            x: { grid: { display: false } }
        }
    }
});

// 6. Revenue Chart
const ctxRev = document.getElementById('revenueChart').getContext('2d');
new Chart(ctxRev, {
    type: 'bar',
    data: {
        labels: ['Basic', 'Standard', 'Premium'],
        datasets: [{
            label: 'Monthly Revenue ($)',
            data: [60000, 120000, 115000],
            backgroundColor: [
                'rgba(229, 9, 20, 0.8)',
                'rgba(58, 134, 255, 0.8)',
                'rgba(56, 176, 0, 0.8)'
            ],
            borderRadius: 6
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { display: false }
        },
        scales: {
            y: { grid: { color: gridColor }, beginAtZero: true },
            x: { grid: { display: false } }
        }
    }
});

// Tab Switching Logic
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-links li');
    const tabContents = document.querySelectorAll('.tab-content');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active from all links
            navLinks.forEach(l => l.classList.remove('active'));
            // Add active to clicked link
            link.classList.add('active');

            // Hide all tabs
            tabContents.forEach(tab => tab.classList.remove('active'));

            // Show target tab
            const targetId = link.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');
        });
    });
});
