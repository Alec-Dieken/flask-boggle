$('form').on('submit', handleForm)

let guesses = new Set();
let time = 60;
let gameActive = true;

async function handleForm(e) {
    e.preventDefault();

    if(gameActive) {
        const guess = $('#guess').val();
    
        const response = await axios({
            url: '/handle',
            method: "POST",
            data: {
            'guess': guess
            }
        });

        const answer = response.data.answer;
        handleAnswer(answer, guess);

        $('#guess').val('');
    }
}

function handleAnswer(ans, guess) {
    if(ans === 'ok' && !guesses.has(guess)) {
        $('#points').text(parseInt($('#points').text()) + guess.length);
        guesses.add(guess);
    }
}

setInterval(handleTimer, 1000);

function handleTimer() {
    if (time == 0) {
        gameActive = false;
        $('#timer').text('Game Over');
    } else {
        time--;
        $('#timer').text(time);
    }
    
}