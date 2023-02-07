#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LENGTH 6

struct package
{
	char* id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package* packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char* name;
	post_office* offices;
	int offices_count;
};

typedef struct town town;



void print_all_packages(town t) {
    printf("%s:\n", t.name);
    for (int office_c = 0; office_c < t.offices_count; office_c++) {
        printf("\t%d:\n", office_c);
        for (int package_c = 0; package_c < t.offices[office_c].packages_count; package_c++) {
            printf("\t\t%s\n", t.offices[office_c].packages[package_c].id);
        }
    }
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {
    post_office *source_post_office = source->offices + source_office_index;
    post_office *target_post_office = target->offices + target_office_index;
    package *new_source_packages = malloc(sizeof(package));
    int new_source_packages_count = 0;

    for (int i = 0; i < source_post_office->packages_count; i++) {
        package the_package = source_post_office->packages[i];
        if ((target_post_office->min_weight <= the_package.weight) &&
            (target_post_office->max_weight >= the_package.weight)) {
                // Target town can receive the package:
                // Add the package to target town
                target_post_office->packages_count++;
                target_post_office->packages = realloc(
                    target_post_office->packages, (target_post_office->packages_count) * sizeof(package)
                );
                target_post_office->packages[target_post_office->packages_count - 1].id = the_package.id;
                target_post_office->packages[target_post_office->packages_count - 1].weight = the_package.weight;
        } else {
            // The package will resend to the Source town
            new_source_packages_count++;
            new_source_packages = realloc(new_source_packages, new_source_packages_count * sizeof(package));
            new_source_packages[new_source_packages_count - 1] = the_package;
        }
    }
    source_post_office->packages = new_source_packages;
    source_post_office->packages_count = new_source_packages_count;
}


town town_with_most_packages(town* towns, int towns_count) {
    town *target_town = NULL;
    int max_packages = 0;
    for (int town_c = 0; town_c < towns_count; town_c++) {
        int packages_num = 0;
        for (int office_c = 0; office_c < towns[town_c].offices_count; office_c++) {
            packages_num += towns[town_c].offices[office_c].packages_count;
        }
        if (packages_num > max_packages) {
            max_packages = packages_num;
            target_town = &towns[town_c];
        }
    }

    return *target_town;
}

town* find_town(town* towns, int towns_count, char* name) {
    for (int i = 0; i < towns_count; i++)
        if (strcmp(towns[i].name, name) == 0)
            return &towns[i];

    return NULL;
}

int main()
{
	int towns_count;
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		scanf("%s", towns[i].name);
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
			scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
				scanf("%s", towns[i].offices[j].packages[k].id);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		scanf("%d", &type);
		switch (type) {
		case 1:
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			scanf("%d", &source_index);
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
			break;
		}
	}
	return 0;
}