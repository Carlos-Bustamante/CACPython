const {createApp} = Vue;

createApp({
    data(){
        return {
            team: null
        }
    },
    mounted(){
        axios
            .get("https://rickandmortyapi.com/api/character")
            .then(
                response => {
                this.team = response.data.results;
            })
            .then( data => {
                console.log(data);
            }).catch(error => console.log(error));
            
    }
    // create(){
    //     fetch("https://rickandmortyapi.com/api")
    //     .then(response => response.json())
    //     .then( data => {
    //         console.log(data);
    //     }).catch(error => console.log(error));
    // }
}).mount("#musicos");