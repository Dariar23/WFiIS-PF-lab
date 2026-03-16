open System

//zad1
let max (x, y) = if x > y then x else y

let min (x, y) = if x < y then x else y

let sum (x, y) = x + y

let diff (x, y) = x - y

let rec eval list =
    match list with
    | (f, (a, b)) :: tail -> 
        let result = f (a, b)
        result :: eval tail
    | [] -> []

let r = [(max, (5, 6)); (sum, (4, -2)); (diff, (4, 9))]
let results = eval r

results |> Seq.iter(printf "%d, ")
printfn("");



//zad2

let l = [("jan", "k", 60); ("ewa", "nowak", 30)]
l |> List.map (fun (imie, _, _) -> imie) |> printfn "Imiona: %A"
l |> List.map (fun (_, _, w) -> float w) |> List.average |> printfn "Średni wiek: %.2f"

let women = l |> List.filter (fun (name, _, _) -> name.[name.Length - 1] = 'a')

printfn "Kobiety: %A" women

l |> List.filter (fun (imie, _, _) -> imie.[imie.Length - 1] <> 'a') |> List.length |> printfn "Ilość mężczyzn: %d"