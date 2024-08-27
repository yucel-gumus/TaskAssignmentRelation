from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class PersonTaskAssignment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    frequency = models.IntegerField()
    last_completion_time = models.DateTimeField()

    @staticmethod
    def get_task_frequencies():
        result = []
        assignments = PersonTaskAssignment.objects.select_related('person', 'task').all()
        for assignment in assignments:
            result.append({
                'task_id': assignment.task.id,
                'task_title': assignment.task.title,
                'person_fullname': f"{assignment.person.first_name} {assignment.person.last_name}",
                'frequency': assignment.frequency
            })
        return result
