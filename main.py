from library import Library


def main():
    lib = Library()

    # Create books
    devu_miskas = lib.create_book("Dievų miškas", "Balys Sruoga", 1957)
    altoriai = lib.create_book("Altorių šešėly", "Vincas Mykolaitis-Putinas", 1933)
    silvelis = lib.create_book("Anykščių šilelis", "Antanas Baranauskas", 1858)

    # Buy copies
    copy1 = lib.add_book(devu_miskas)
    copy2 = lib.add_book(devu_miskas)
    copy3 = lib.add_book(altoriai)
    lib.add_book(silvelis)

    print("=== Library after buying copies ===")
    for result in lib.search("Balys Sruoga"):
        print(f"  {result}")
    for result in lib.search("Vincas Mykolaitis-Putinas"):
        print(f"  {result}")
    for result in lib.search("Antanas Baranauskas"):
        print(f"  {result}")

    # Borrow a book
    borrowed = lib.borrow_book(devu_miskas)
    print(f"\nBorrowed: {borrowed}")

    # Borrow second copy
    borrowed2 = lib.borrow_book(devu_miskas)
    print(f"Borrowed: {borrowed2}")

    # Try borrowing when none available
    print("\nTrying to borrow 'Dievų miškas' again...")
    try:
        lib.borrow_book(devu_miskas)
    except ValueError as e:
        print(f"  Error: {e}")

    # Return a copy
    lib.return_book(borrowed)
    print(f"\nReturned: {borrowed}")

    # Search by title
    print("\n=== Search: 'Dievų miškas' ===")
    for result in lib.search("Dievų miškas"):
        print(f"  {result}")

    # Search by author
    print("\n=== Search: 'Vincas Mykolaitis-Putinas' ===")
    for result in lib.search("Vincas Mykolaitis-Putinas"):
        print(f"  {result}")

    # Search with no results
    print("\n=== Search: 'Nežinoma knyga' ===")
    results = lib.search("Nežinoma knyga")
    print(f"  Found: {len(results)} results")


if __name__ == "__main__":
    main()
