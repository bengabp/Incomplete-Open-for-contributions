$(document).ready(()=>{
    $.ajax({
        url:"/get-facts",
        type:'GET',
        success:(response) => {
            $("#facts-container").empty();
            let unique_hashes = response.unique_hashes;
            response.results.forEach(element => {
                let starBtn = document.createElement('button');
                starBtn.classList.add("starbtn")
                let hash = generateHash(element.fact);
                starBtn.innerHTML = `<i class="fa-regular fa-star" onclick="starMentalItem(this)" data-hash="star_${hash}" style="color:${unique_hashes.includes(hash) ? 'var(--icon-button-bg-color)':'var(--icon-normal-color)'};cursor:pointer;"></i>`;
                

                $("#facts-container").append(`
                    <div class="fit-workout-vid fact-item" data-hash="main_${hash}" data-mental-category='fact'>
                        <div style='display:flex;gap:20px;align-items:cener;'>
                            <span class='mental-cat-label'>Fact</span>
                            ${starBtn.innerHTML}
                        </div>
                        <p>
                            ${element.fact}
                        </p>
                    </div>
                `)
                // starBtn.addEventListener("click",starMentalItem)
            });
        }
    });

    $.ajax({
        url:"/get-riddles",
        type:'GET',
        success:(response) => {
            $("#riddles-container").empty();
            let unique_hashes = response.unique_hashes;
            response.results.forEach(element => {
                let starBtn = document.createElement('button');
                let hash = generateHash(element.question+element.answer);
                starBtn.innerHTML = `<i class="fa-regular fa-star" onclick="starMentalItem(this)" data-hash="star_${hash}" style="color:${unique_hashes.includes(hash) ? 'var(--icon-button-bg-color)':'var(--icon-normal-color)'};cursor:pointer;"></i>`;                    
                $("#riddles-container").append(`
                    <div class="fit-workout-vid quote-item" data-hash="main_${hash}" data-mental-category='riddle'>
                        <div style='display:flex;gap:20px;align-items:cener;'>
                            <span class='mental-cat-label'>Riddle</span>
                            ${starBtn.innerHTML}
                        </div>
                        <p>
                            ${element.question}
                        </p>
                        <span class="mental-cat-quote-author mental-cat-label">${element.answer}</span>
                    </div>
                `)
            });
        }
    });

    $.ajax({
        url:"/get-jokes",
        type:'GET',
        success:(response) => {
            $("#jokes-container").empty();
            let unique_hashes = response.unique_hashes;
            response.results.forEach(element => {
                let starBtn = document.createElement('button');
                let hash = generateHash(element.joke);
                starBtn.innerHTML = `<i class="fa-regular fa-star" onclick="starMentalItem(this)" data-hash="star_${hash}" style="color:${unique_hashes.includes(hash) ? 'var(--icon-button-bg-color)':'var(--icon-normal-color)'};cursor:pointer;"></i>`;                    
                if (element.joke){
                    $("#jokes-container").append(`
                        <div class="fit-workout-vid quote-item" data-hash="main_${hash}" data-mental-category='joke'>
                            <div style='display:flex;gap:20px;align-items:cener;'>
                                <span class='mental-cat-label'>Joke</span>
                                ${starBtn.innerHTML}
                            </div>
                            <p>
                                ❝${element.joke}❞
                            </p>
                        </div>
                    `)
                }
            });
        }
    });

    $.ajax({
        url:"/get-quotes",
        type:'GET',
        success:(response) => {
            let unique_hashes = response.unique_hashes;
            $("#quotes-container").empty();
            response.results.forEach(element => {
                let starBtn = document.createElement('button');
                let hash = generateHash(element.quote+element.author);
                starBtn.innerHTML = `<i class="fa-regular fa-star" onclick="starMentalItem(this)" data-hash="star_${hash}" style="color:${unique_hashes.includes(hash) ? 'var(--icon-button-bg-color)':'var(--icon-normal-color)'};cursor:pointer;"></i>`;                $("#quotes-container").append(`
                    <div class="fit-workout-vid quote-item" data-hash="main_${hash}" data-mental-category='quote'>
                        <div style='display:flex;gap:20px;align-items:cener;'>
                            <span class='mental-cat-label'>Quote</span>
                            ${starBtn.innerHTML}
                        </div>
                        <p>
                            ❝${element.quote}❞
                        </p>
                        <span class="mental-cat-quote-author mental-cat-label">${element.author}</span>
                    </div>
                `)
            });
        }
    });

    function generateHash(obj) {
        let hash = CryptoJS.MD5(obj);
        return hash.toString(CryptoJS.enc.Hex);
    }

})

function starMentalItem(starBtn){
    let hash = starBtn.attributes["data-hash"].value.split("_")[1];
    let parentElement = document.querySelector(`div[data-hash='main_${hash}']`);
    let parentElementCategory = parentElement.attributes.getNamedItem("data-mental-category").value;

    // data.append('csrfmiddlewaretoken', document.querySelector('input[name="csrfmiddlewaretoken"]').value);    

    if (parentElementCategory === "fact"){
        let fact = parentElement.querySelector("p").textContent.trim();
        let formData = new FormData();
        formData.append("fact",fact);
        formData.append("category",parentElementCategory);
        formData.append("hash",hash);
        
        starBtn.disabled = true;
        $.ajax({
            url:"/favourites",
            type:"POST",
            data:formData,
            processData: false,
            contentType: false,
            success:(response)=>{
                starBtn.style.color = "var(--icon-button-bg-color)"
            },
            complete:()=>{
                console.log("completed")
                starBtn.disabled = false;
            }
        });

    } else if (parentElementCategory === "joke"){
        let joke = parentElement.querySelector("p").textContent.trim();
        let formData = new FormData();
        formData.append("joke",joke);
        formData.append("category",parentElementCategory);
        formData.append("hash",hash);

        starBtn.disabled = true;
        $.ajax({
            url:"/favourites",
            type:"POST",
            data:formData,
            processData: false,
            contentType: false,
            success:(response)=>{
                starBtn.style.color = "var(--icon-button-bg-color)"
            },
            complete:()=>{
                console.log("completed")
                starBtn.disabled = false;
            }
        });

    } else if (parentElementCategory === "riddle"){
        let riddle = parentElement.querySelector("p").textContent.trim();
        let answer = parentElement.querySelector("span:last-child").textContent.trim();
        
        let formData = new FormData();
        formData.append("riddle",riddle);
        formData.append("answer",answer);
        formData.append("category",parentElementCategory);
        formData.append("hash",hash);

        starBtn.disabled = true;
        $.ajax({
            url:"/favourites",
            type:"POST",
            data:formData,
            processData: false,
            contentType: false,
            success:(response)=>{
                starBtn.style.color = "var(--icon-button-bg-color)"
            },
            complete:()=>{
                console.log("completed")
                starBtn.disabled = false;
            }
        });

    } else if (parentElementCategory === "quote"){
        let quote = parentElement.querySelector("p").textContent.trim();
        let author = parentElement.querySelector("span:last-child").textContent.trim();
        let payload = {
            'quote':quote,
            'author':author,
            'hash':hash,
            'caregory':parentElementCategory
        }
        let formData = new FormData();
        formData.append("quote",quote);
        formData.append("author",author);
        formData.append("category",parentElementCategory);
        formData.append("hash",hash);

        starBtn.disabled = true;

        starBtn.disabled = true;
        $.ajax({
            url:"/favourites",
            type:"POST",
            data:formData,
            processData: false,
            contentType: false,
            success:(response)=>{
                starBtn.style.color = "var(--icon-button-bg-color)"
            },
            complete:()=>{
                console.log("completed")
                starBtn.disabled = false;
            }
        });
    } else {
        console.log("Invalid category");
    }    
}

function scrollToSec(id){
    document.getElementById(id).scrollIntoView({behavior:"smooth"});
}