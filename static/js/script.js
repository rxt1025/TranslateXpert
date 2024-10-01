document.getElementById("translateBtn").addEventListener("click",() => {

    const sourceText = document.getElementById("sourceText").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;

    if (sourceText.trim() !== ""){
        translateText(sourceText, sourceLang, targetLang);
    }
});


async function translateText(text, sourceLang, targetLang){

    const response = await fetch("/translate",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text:text,
            sourceLang: sourceLang,
            targetLang: targetLang
        })
    
    
    });

    if(response.ok){
        const data = await response.json();
        document.getElementById("translatedText").value = data.translatedText || "Translation not found.";
    } else {
        console.error("Translation API error:", response.status, response.statusText, await response.json());
    }

}

