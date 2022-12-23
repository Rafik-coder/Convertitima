function copyText() {
    // Select the text to be copied
    var text = document.querySelector('#text');
    text.select();

    // Copy the text to the clipboard
    console.log(document.execCommand('copy'));
    alert("copied")
  }