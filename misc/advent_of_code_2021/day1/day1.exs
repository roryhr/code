defmodule Day1 do
  def parse_file(path) do
    path
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  def is_greater([first, second, _]) do
    if first > second do
      1
    else
      0
    end
  end
end

"input.txt"
|> Day1.parse_file()
|> Day1.is_greater()
|> IO.inspect()
