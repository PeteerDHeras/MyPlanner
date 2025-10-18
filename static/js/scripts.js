document.addEventListener('DOMContentLoaded', function () {
  const calendarEl = document.getElementById('calendar');
  if (!calendarEl) {
    console.warn("⚠️ No existe el contenedor #calendar");
    return;
  }

  const calendar = new FullCalendar.Calendar(calendarEl, {
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    firstDay: 1,
    initialView: 'dayGridWeek',

    activeStart: 2,
    selectable: true,
    editable: true,
    events: [
      { title: 'Reunión', start: new Date(), end: Date(19-6-2024) },
    ]
  });

  calendar.render();
  console.log("Calendar renderizado");
});
