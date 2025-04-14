import os
from django.core.management.base import BaseCommand
from django.conf import settings
from generator.models import Template
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'Creates initial portfolio templates in the database'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating portfolio templates...'))
        
        # Check if templates already exist
        if Template.objects.exists():
            self.stdout.write(self.style.WARNING('Templates already exist in the database. Skipping creation.'))
            return
        
        # Create Template 1 - Professional
        template1 = Template(
            name="Professional Blue",
            description="A clean, professional template with a blue color scheme, perfect for job seekers in corporate environments."
        )
        
        # Create Template 2 - Modern
        template2 = Template(
            name="Modern Minimalist",
            description="A modern, minimalist template with a dark header and timeline layout, ideal for creative professionals."
        )
        
        # Save templates first (required before we can assign images)
        template1.save()
        template2.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created template: {template1.name}'))
        self.stdout.write(self.style.SUCCESS(f'Created template: {template2.name}'))
        
        # Create sample preview images if they don't exist
        try:
            # For template 1 - create a blue preview
            img_content1 = self._generate_color_image(800, 600, (65, 105, 225))  # Royal Blue
            template1.preview_image.save('template1_preview.png', ContentFile(img_content1), save=True)
            
            # For template 2 - create a dark preview
            img_content2 = self._generate_color_image(800, 600, (44, 62, 80))  # Dark Slate
            template2.preview_image.save('template2_preview.png', ContentFile(img_content2), save=True)
            
            self.stdout.write(self.style.SUCCESS('Added preview images to templates'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Could not create preview images: {e}'))

        self.stdout.write(self.style.SUCCESS('Finished creating portfolio templates'))
    
    def _generate_color_image(self, width, height, color):
        """
        Generate a solid color image using Pillow.
        Returns the image bytes that can be saved to a file.
        """
        try:
            from PIL import Image
            import io
            
            # Create a new image with the specified color
            img = Image.new('RGB', (width, height), color)
            
            # Save the image to a bytes buffer
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            
            return buffer.getvalue()
        except ImportError:
            self.stdout.write(self.style.WARNING('Pillow library not available, cannot generate preview images'))
            # Return a small empty PNG as fallback
            return b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xdc\xccY\xe7\x00\x00\x00\x00IEND\xaeB`\x82'