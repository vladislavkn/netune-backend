from shared.models import Author, Track


def format_info_prompt(tracks: list[Track], authors: list[Author]) -> str:
    tracks_list = "\n".join(
        map(lambda track: f"- {track.name} ({', '.join(track.authors)})", tracks))
    authors_list = "\n".join(
        map(lambda author: f"- {author.name} ({', '.join(author.genres)})", authors))

    return f"Now answer for this text:\nThe list of the tracks with authors in the brackets:\n{tracks_list}\n" + \
        f"The list of the artists with their genres in brackets:\n{authors_list}"
