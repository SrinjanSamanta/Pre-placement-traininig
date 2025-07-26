#include <stdio.h>

int main() {
    int arr[100], n, element;

    printf("Enter number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Array before insertion: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nEnter the element to insert at the end: ");
    scanf("%d", &element);

    arr[n] = element;
    n++;

    printf("Array after insertion: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}

