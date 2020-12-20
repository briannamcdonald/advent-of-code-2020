def get_tiles(data):
    tiles = {}
    curr_tile = []
    key = ""
    for line in data:
        if line == "":
            tiles[key] = curr_tile
            curr_tile = []
        elif line.split()[0] == "Tile":
            key = line[:-1]
        else:
            curr_tile.append(line)
    return tiles


def get_tile_edges(tiles):
    tile_edges_dict = {}
    for tile_key in tiles:
        tile_info = tiles[tile_key]
        # horizontal edges
        tile_edges = [tile_info[0], tile_info[len(tile_info) - 1]]
        # vertical edges
        left_edge = ""
        for i in range(10):
            left_edge += tile_info[i][0]
        tile_edges.append(left_edge)
        right_edge = ""
        for i in range(10):
            right_edge += tile_info[i][9]
        tile_edges.append(right_edge)
        tile_edges_dict[tile_key] = tile_edges
    return tile_edges_dict


def get_edge_match_count(tile_edges_dict):
    num_matching = {}
    for curr_tile_key in tile_edges_dict:
        curr_tile_edges = tile_edges_dict[curr_tile_key]
        for tile_key in tile_edges_dict:
            tile_edges = tile_edges_dict[tile_key]
            for curr_edge in curr_tile_edges:
                for edge in tile_edges:
                    if curr_tile_key == tile_key:
                        continue
                    if (
                        curr_edge == edge
                        or curr_edge[::-1] == edge
                        or curr_edge == edge[::-1]
                        or curr_edge[::-1] == edge[::-1]
                    ):
                        try:
                            num_matching[curr_tile_key] += 1
                        except:
                            num_matching[curr_tile_key] = 1
    return num_matching


def main():
    data = open("day20/input.txt", "r")
    data = [line.strip() for line in data]

    tiles = get_tiles(data)
    tile_edges_dict = get_tile_edges(tiles)
    # for each tile, check how many other tiles have edges that match its edges
    num_matching = get_edge_match_count(tile_edges_dict)
    # find the tiles that have edges that only match two other tiles since they must be corners
    answer = 1
    for tile_key in num_matching:
        if num_matching[tile_key] == 2:
            answer *= int(tile_key.split()[1])
    print(answer)


if __name__ == "__main__":
    main()