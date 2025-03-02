<script type="text/javascript">
    setInterval(function() {
        var timeLeft = document.getElementById("timeLeft");
        var minutesLeft = parseInt(timeLeft.innerText);
        if (minutesLeft > 0) {
            timeLeft.innerText = minutesLeft - 1;
        }
    }, 60000);  // Update every minute
</script>
