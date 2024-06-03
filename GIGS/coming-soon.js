// Set the days to 46
const days = 46;
const hours = 0;
const minutes = 0;
const seconds = 0;

// Calculate the countdown date based on the set days, hours, minutes, and seconds
const countdownDate = new Date(Date.now() + days * 24 * 60 * 60 * 1000 + hours * 60 * 60 * 1000 + minutes * 60 * 1000 + seconds * 1000);

// Update the countdown every second
const countdownTimer = setInterval(function() {
    // Get the current date and time
    const now = new Date().getTime();
    
    // Calculate the time remaining
    const timeRemaining = countdownDate - now;

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Update the countdown display
    document.getElementById("days").innerText = formatTime(days);
    document.getElementById("hours").innerText = formatTime(hours);
    document.getElementById("minutes").innerText = formatTime(minutes);
    document.getElementById("seconds").innerText = formatTime(seconds);

    // If the countdown is over, stop the timer
    if (timeRemaining < 0) {
        clearInterval(countdownTimer);
    }
}, 1000);

// Function to add leading zeros to single-digit numbers
function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}