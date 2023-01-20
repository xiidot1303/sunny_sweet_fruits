//======= Soundly Button Scripts =======

    function ding() {
    var sound = new Audio(
        "https://www.soundjay.com/misc/sounds/small-bell-ring-01a.mp3"
    );
    sound.play();
    }

    document
    .getElementById("button123")
    .addEventListener("click", ding);
        function ding() {
    var sound = new Audio(
        "https://www.soundjay.com/misc/sounds/small-bell-ring-01a.mp3"
    );
    sound.play();
    };
    // second close sound
    function ding2() {
    var sound2 = new Audio(
      "https://www.soundjay.com/buttons/sounds/button-30.mp3"
    );
    sound2.play();
    }

    document
    .getElementById("button11")
    .addEventListener("click", ding2);