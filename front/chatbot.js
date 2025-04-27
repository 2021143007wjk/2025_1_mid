document.addEventListener('DOMContentLoaded', function () {
    const chatWindow = document.getElementById('chat-window');
    const inputForm = document.getElementById('input-form');
    const userInput = document.getElementById('user-input');
  
    // 메시지 추가 함수
    function appendMessage(text, sender, isTyping = false) {
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('message', sender);

      if (isTyping) {
        const typingSpan = document.createElement('span');
        typingSpan.classList.add('typing');
        messageDiv.appendChild(typingSpan);
      } else {
        messageDiv.textContent = text;
      }
    
      chatWindow.appendChild(messageDiv);
      chatWindow.scrollTop = chatWindow.scrollHeight;
    
      return messageDiv;
    }
  
    // 사용자 입력 전송 이벤트
    inputForm.addEventListener('submit', async function (e) {
      e.preventDefault();
      const message = userInput.value.trim();
      if (message === '') return;
    
      appendMessage(message, 'user');
      userInput.value = '';
    
      // "..." 애니메이션 말풍선 추가
      const botMessage = appendMessage('', 'bot', true);
    
      try {
        const response = await fetch('http://localhost:8000/chatbot', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ text: message })
        });
    
        if (!response.ok) {
          throw new Error('서버 응답 오류');
        }
    
        const data = await response.json();
        
        // 기존 botMessage의 애니메이션 지우고 실제 텍스트로 교체
        botMessage.classList.remove('typing');
        botMessage.textContent = data.result;
        console.log(data.result)
    
      } catch (error) {
        console.error('에러 발생:', error);
        botMessage.classList.remove('typing');
        botMessage.textContent = '오류가 발생했습니다. 다시 시도해 주세요.';
      }
    });    
  });
  