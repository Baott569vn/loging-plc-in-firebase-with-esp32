var webSocket = new WebSocket('ws://192.168.1.4:81');

webSocket.onmessage = function(event) {
    var serialData = event.data;
    var logContainer = document.getElementById('logContainer');
    var logEntry = document.createElement('div');
    logEntry.classList.add('logEntry'); // Thêm lớp cho hàng

    logEntry.textContent = serialData;

    // Highlight các từ khóa
    logEntry.innerHTML = logEntry.innerHTML.replace(/(ERROR|CHANGE|BEYOND LIMIT|REQUEST ACT RIGHT NOW)/g, "<span class='highlighted'>$1</span>");

    // Thêm sự kiện mouseover và mouseout
    logEntry.addEventListener('mouseover', function() {
        this.classList.add('highlightOnHover');
    });

    logEntry.addEventListener('mouseout', function() {
        this.classList.remove('highlightOnHover');
    });

    logContainer.appendChild(logEntry);

    // Cuộn xuống cuối của khung nhật ký
    logContainer.scrollTop = logContainer.scrollHeight;
};

function toggleTheme() {
    var body = document.body;
    body.classList.toggle('dark-theme');
}
