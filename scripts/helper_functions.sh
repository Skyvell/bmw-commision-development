find_path_ending_with() {
  local path="$1"
  local end_condition="$2"

  while [[ "$(basename "$path")" != "$end_condition" && "$path" != "/" ]]; do
    path=$(dirname "$path")
  done

  echo "$path"
}
