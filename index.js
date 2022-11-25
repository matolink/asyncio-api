async function fetchPKMN(number) {
  pokemon = await fetch(`https://pokeapi.co/api/v2/pokemon/` + number)
  pokemonJSON = await pokemon.json()
  return pokemonJSON
}
async function main() {
  let elements = 15
  let urls = [...Array(elements)].map((item, index) => index + 1)
  let promises = []
  for (let index = 0; index < urls.length; index++) {
    promises.push(fetchPKMN(index + 1))
  }
  let allPKMN = await Promise.all(promises)
  console.log(allPKMN)
}

main()
