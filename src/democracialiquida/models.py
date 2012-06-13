from django.db import models


class LiquidFeedbackVersion(models.Model):
    string = models.TextField(blank=True)
    major = models.IntegerField(null=True, blank=True)
    minor = models.IntegerField(null=True, blank=True)
    revision = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'liquid_feedback_version'


class SystemSetting(models.Model):
    member_ttl = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'system_setting'


class Contingent(models.Model):
    time_frame = models.TextField(primary_key=True) # This field type is a guess.
    text_entry_limit = models.IntegerField(null=True, blank=True)
    initiative_limit = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'contingent'


class MemberApplication(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    member = models.ForeignKey('Member')
    name = models.TextField()
    comment = models.TextField(blank=True)
    access_level = models.TextField() # This field type is a guess.
    key = models.TextField(unique=True)
    last_usage = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'member_application'


class MemberHistory(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    member = models.ForeignKey('Member')
    until = models.DateTimeField()
    active = models.BooleanField()
    name = models.TextField()
    class Meta:
        db_table = u'member_history'


class RenderedMemberStatement(models.Model):
    member = models.ForeignKey('Member')
    format = models.TextField()
    content = models.TextField()
    class Meta:
        db_table = u'rendered_member_statement'


class Setting(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'setting'


class SettingMap(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    subkey = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'setting_map'


class MemberRelationSetting(models.Model):
    member = models.ForeignKey('Member', related_name="member_relation_settings")
    key = models.TextField()
    other_member = models.ForeignKey('Member')
    value = models.TextField()
    class Meta:
        db_table = u'member_relation_setting'


class MemberImage(models.Model):
    member = models.ForeignKey('Member')
    image_type = models.TextField() # This field type is a guess.
    scaled = models.BooleanField()
    content_type = models.TextField(blank=True)
    data = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'member_image'


class MemberCount(models.Model):
    calculated = models.DateTimeField()
    total_count = models.IntegerField()
    class Meta:
        db_table = u'member_count'


class Contact(models.Model):
    member = models.ForeignKey('Member', related_name="contacts")
    other_member = models.ForeignKey('Member')
    public = models.BooleanField()
    class Meta:
        db_table = u'contact'


class IgnoredMember(models.Model):
    member = models.ForeignKey('Member', related_name="ignored_members")
    other_member = models.ForeignKey('Member')
    class Meta:
        db_table = u'ignored_member'


class Session(models.Model):
    ident = models.TextField(primary_key=True)
    additional_secret = models.TextField(blank=True)
    expiry = models.DateTimeField()
    member = models.ForeignKey('Member', null=True, blank=True)
    lang = models.TextField(blank=True)
    class Meta:
        db_table = u'session'


class UnitSetting(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    unit = models.ForeignKey('Unit')
    value = models.TextField()
    class Meta:
        db_table = u'unit_setting'


class AreaSetting(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    area = models.ForeignKey('Area')
    value = models.TextField()
    class Meta:
        db_table = u'area_setting'


class AllowedPolicy(models.Model):
    area = models.ForeignKey('Area', unique=True)
    policy = models.ForeignKey('Policy')
    default_policy = models.BooleanField()
    class Meta:
        db_table = u'allowed_policy'


class Policy(models.Model):
    #id = models.IntegerField(primary_key=True)
    index = models.IntegerField()
    active = models.BooleanField()
    name = models.TextField(unique=True)
    description = models.TextField()
    admission_time = models.TextField() # This field type is a guess.
    discussion_time = models.TextField() # This field type is a guess.
    verification_time = models.TextField() # This field type is a guess.
    voting_time = models.TextField() # This field type is a guess.
    issue_quorum_num = models.IntegerField()
    issue_quorum_den = models.IntegerField()
    initiative_quorum_num = models.IntegerField()
    initiative_quorum_den = models.IntegerField()
    direct_majority_num = models.IntegerField()
    direct_majority_den = models.IntegerField()
    direct_majority_strict = models.BooleanField()
    direct_majority_positive = models.IntegerField()
    direct_majority_non_negative = models.IntegerField()
    indirect_majority_num = models.IntegerField()
    indirect_majority_den = models.IntegerField()
    indirect_majority_strict = models.BooleanField()
    indirect_majority_positive = models.IntegerField()
    indirect_majority_non_negative = models.IntegerField()
    no_reverse_beat_path = models.BooleanField()
    no_multistage_majority = models.BooleanField()
    class Meta:
        db_table = u'policy'


class IssueSetting(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    issue = models.ForeignKey('Issue')
    value = models.TextField()
    class Meta:
        db_table = u'issue_setting'


class Battle(models.Model):
    issue = models.ForeignKey('Initiative')
    winning_initiative_id = models.IntegerField(null=True, blank=True)
    losing_initiative_id = models.IntegerField(null=True, blank=True)
    count = models.IntegerField()
    class Meta:
        db_table = u'battle'


class IgnoredInitiative(models.Model):
    initiative = models.ForeignKey('Initiative')
    member = models.ForeignKey('Member')
    class Meta:
        db_table = u'ignored_initiative'


class InitiativeSetting(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    initiative = models.ForeignKey('Initiative')
    value = models.TextField()
    class Meta:
        db_table = u'initiative_setting'


class RenderedDraft(models.Model):
    draft = models.ForeignKey('Draft')
    format = models.TextField()
    content = models.TextField()
    class Meta:
        db_table = u'rendered_draft'


class RenderedSuggestion(models.Model):
    suggestion = models.ForeignKey('Suggestion')
    format = models.TextField()
    content = models.TextField()
    class Meta:
        db_table = u'rendered_suggestion'


class SuggestionSetting(models.Model):
    member = models.ForeignKey('Member')
    key = models.TextField()
    suggestion = models.ForeignKey('Suggestion')
    value = models.TextField()
    class Meta:
        db_table = u'suggestion_setting'


class Privilege(models.Model):
    unit = models.ForeignKey('Unit')
    member = models.ForeignKey('Member')
    admin_manager = models.BooleanField()
    unit_manager = models.BooleanField()
    area_manager = models.BooleanField()
    voting_right_manager = models.BooleanField()
    voting_right = models.BooleanField()
    class Meta:
        db_table = u'privilege'


class Membership(models.Model):
    area = models.ForeignKey('Area')
    member = models.ForeignKey('Member')
    class Meta:
        db_table = u'membership'


class Initiator(models.Model):
    initiative = models.ForeignKey('Initiative')
    member = models.ForeignKey('Member')
    accepted = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = u'initiator'


class Unit(models.Model):
    #id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    active = models.BooleanField()
    name = models.TextField()
    description = models.TextField()
    member_count = models.IntegerField(null=True, blank=True)
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'unit'


class Area(models.Model):
    #id = models.IntegerField(primary_key=True)
    unit = models.ForeignKey('Unit')
    active = models.BooleanField()
    name = models.TextField()
    description = models.TextField()
    direct_member_count = models.IntegerField(null=True, blank=True)
    member_weight = models.IntegerField(null=True, blank=True)
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'area'


class Delegation(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    truster = models.ForeignKey('Member', related_name="delegations")
    trustee = models.ForeignKey('Member', null=True, blank=True)
    scope = models.TextField() # This field type is a guess.
    unit = models.ForeignKey('Unit', null=True, blank=True)
    area = models.ForeignKey('Area', null=True, blank=True)
    issue = models.ForeignKey('Issue', null=True, blank=True)
    class Meta:
        db_table = u'delegation'


class DirectPopulationSnapshot(models.Model):
    issue = models.ForeignKey('Issue')
    event = models.TextField() # This field type is a guess.
    member = models.ForeignKey('Member')
    weight = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'direct_population_snapshot'


class DelegatingPopulationSnapshot(models.Model):
    issue = models.ForeignKey('Issue')
    event = models.TextField() # This field type is a guess.
    member = models.ForeignKey('Member')
    weight = models.IntegerField(null=True, blank=True)
    scope = models.TextField() # This field type is a guess.
    delegate_member_ids = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'delegating_population_snapshot'


class DelegatingInterestSnapshot(models.Model):
    issue = models.ForeignKey('Issue')
    event = models.TextField() # This field type is a guess.
    member = models.ForeignKey('Member')
    weight = models.IntegerField(null=True, blank=True)
    scope = models.TextField() # This field type is a guess.
    delegate_member_ids = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'delegating_interest_snapshot'


class DirectInterestSnapshot(models.Model):
    issue = models.ForeignKey('Issue')
    event = models.TextField() # This field type is a guess.
    member = models.ForeignKey('Member')
    weight = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'direct_interest_snapshot'


class DirectSupporterSnapshot(models.Model):
    issue = models.ForeignKey('Initiative')
    initiative = models.ForeignKey('Draft')
    event = models.TextField() # This field type is a guess.
    member = models.ForeignKey('Member')
    draft_id = models.BigIntegerField()
    informed = models.BooleanField()
    satisfied = models.BooleanField()
    class Meta:
        db_table = u'direct_supporter_snapshot'


class NonVoter(models.Model):
    issue = models.ForeignKey('Issue')
    member = models.ForeignKey('Member')
    class Meta:
        db_table = u'non_voter'


class IssueComment(models.Model):
    issue = models.ForeignKey('Issue')
    member = models.ForeignKey('Member')
    changed = models.DateTimeField()
    formatting_engine = models.TextField(blank=True)
    content = models.TextField()
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'issue_comment'


class RenderedIssueComment(models.Model):
    issue = models.ForeignKey('IssueComment')
    member_id = models.IntegerField()
    format = models.TextField()
    content = models.TextField()
    class Meta:
        db_table = u'rendered_issue_comment'


class VotingComment(models.Model):
    issue = models.ForeignKey('Issue')
    member = models.ForeignKey('Member')
    changed = models.DateTimeField(null=True, blank=True)
    formatting_engine = models.TextField(blank=True)
    content = models.TextField()
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'voting_comment'


class RenderedVotingComment(models.Model):
    issue = models.ForeignKey('VotingComment')
    member_id = models.IntegerField()
    format = models.TextField()
    content = models.TextField()
    class Meta:
        db_table = u'rendered_voting_comment'


class Event(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    occurrence = models.DateTimeField()
    event = models.TextField() # This field type is a guess.
    member = models.ForeignKey('Member', null=True, blank=True)
    issue = models.ForeignKey('Issue', null=True, blank=True)
    state = models.TextField(blank=True) # This field type is a guess.
    initiative = models.ForeignKey('Draft', null=True, blank=True)
    draft_id = models.BigIntegerField(null=True, blank=True)
    suggestion_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'event'


class NotificationSent(models.Model):
    event_id = models.BigIntegerField()
    class Meta:
        db_table = u'notification_sent'


class Member(models.Model):
    #id = models.IntegerField(primary_key=True)
    user = models.OneToOneField('auth.User')
    created = models.DateTimeField()
    invite_code = models.TextField(unique=True, blank=True)
    invite_code_expiry = models.DateTimeField(null=True, blank=True)
    admin_comment = models.TextField(blank=True)
    activated = models.DateTimeField(null=True, blank=True)
    last_activity = models.DateField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    login = models.TextField(unique=True, blank=True)
    password = models.TextField(blank=True)
    locked = models.BooleanField()
    active = models.BooleanField()
    admin = models.BooleanField()
    lang = models.TextField(blank=True)
    notify_email = models.TextField(blank=True)
    notify_email_unconfirmed = models.TextField(blank=True)
    notify_email_secret = models.TextField(unique=True, blank=True)
    notify_email_secret_expiry = models.DateTimeField(null=True, blank=True)
    notify_email_lock_expiry = models.DateTimeField(null=True, blank=True)
    notify_level = models.TextField(blank=True) # This field type is a guess.
    password_reset_secret = models.TextField(unique=True, blank=True)
    password_reset_secret_expiry = models.DateTimeField(null=True, blank=True)
    name = models.TextField(unique=True, blank=True)
    identification = models.TextField(unique=True, blank=True)
    authentication = models.TextField(blank=True)
    organizational_unit = models.TextField(blank=True)
    internal_posts = models.TextField(blank=True)
    realname = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    email = models.TextField(blank=True)
    xmpp_address = models.TextField(blank=True)
    website = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    mobile_phone = models.TextField(blank=True)
    profession = models.TextField(blank=True)
    external_memberships = models.TextField(blank=True)
    external_posts = models.TextField(blank=True)
    formatting_engine = models.TextField(blank=True)
    statement = models.TextField(blank=True)
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'member'


class Draft(models.Model):
    initiative = models.ForeignKey('Initiative')
    #id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField()
    author = models.ForeignKey('Member')
    formatting_engine = models.TextField(blank=True)
    content = models.TextField()
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'draft'


class Issue(models.Model):
    #id = models.IntegerField(primary_key=True)
    area = models.ForeignKey('Area')
    policy = models.ForeignKey('Policy')
    state = models.TextField() # This field type is a guess.
    created = models.DateTimeField()
    accepted = models.DateTimeField(null=True, blank=True)
    half_frozen = models.DateTimeField(null=True, blank=True)
    fully_frozen = models.DateTimeField(null=True, blank=True)
    closed = models.DateTimeField(null=True, blank=True)
    ranks_available = models.BooleanField()
    cleaned = models.DateTimeField(null=True, blank=True)
    admission_time = models.TextField() # This field type is a guess.
    discussion_time = models.TextField() # This field type is a guess.
    verification_time = models.TextField() # This field type is a guess.
    voting_time = models.TextField() # This field type is a guess.
    snapshot = models.DateTimeField(null=True, blank=True)
    latest_snapshot_event = models.TextField(blank=True) # This field type is a guess.
    population = models.IntegerField(null=True, blank=True)
    voter_count = models.IntegerField(null=True, blank=True)
    status_quo_schulze_rank = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issue'


class Suggestion(models.Model):
    initiative = models.ForeignKey('Initiative')
    #id = models.BigIntegerField(primary_key=True)
    draft_id = models.BigIntegerField()
    created = models.DateTimeField()
    author = models.ForeignKey('Member')
    name = models.TextField()
    formatting_engine = models.TextField(blank=True)
    content = models.TextField()
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    minus2_unfulfilled_count = models.IntegerField(null=True, blank=True)
    minus2_fulfilled_count = models.IntegerField(null=True, blank=True)
    minus1_unfulfilled_count = models.IntegerField(null=True, blank=True)
    minus1_fulfilled_count = models.IntegerField(null=True, blank=True)
    plus1_unfulfilled_count = models.IntegerField(null=True, blank=True)
    plus1_fulfilled_count = models.IntegerField(null=True, blank=True)
    plus2_unfulfilled_count = models.IntegerField(null=True, blank=True)
    plus2_fulfilled_count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'suggestion'


class UnitDelegation(models.Model):
    unit_id = models.IntegerField(null=True, blank=True)
    #id# = models.BigIntegerField(null=True, blank=True)
    truster_id = models.IntegerField(null=True, blank=True)
    trustee_id = models.IntegerField(null=True, blank=True)
    scope = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'unit_delegation'


class AreaDelegation(models.Model):
    area_id = models.IntegerField(null=True, blank=True)
    #id# = models.BigIntegerField(null=True, blank=True)
    truster_id = models.IntegerField(null=True, blank=True)
    trustee_id = models.IntegerField(null=True, blank=True)
    scope = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'area_delegation'


class IssueDelegation(models.Model):
    issue_id = models.IntegerField(null=True, blank=True)
    #id# = models.BigIntegerField(null=True, blank=True)
    truster_id = models.IntegerField(null=True, blank=True)
    trustee_id = models.IntegerField(null=True, blank=True)
    scope = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'issue_delegation'


class MemberCountView(models.Model):
    total_count = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'member_count_view'


class UnitMemberCount(models.Model):
    unit_id = models.IntegerField(null=True, blank=True)
    member_count = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'unit_member_count'


class AreaMemberCount(models.Model):
    area_id = models.IntegerField(null=True, blank=True)
    direct_member_count = models.BigIntegerField(null=True, blank=True)
    member_weight = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'area_member_count'


class OpeningDraft(models.Model):
    initiative_id = models.IntegerField(null=True, blank=True)
    #id# = models.BigIntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    author_id = models.IntegerField(null=True, blank=True)
    formatting_engine = models.TextField(blank=True)
    content = models.TextField(blank=True)
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'opening_draft'


class CurrentDraft(models.Model):
    initiative_id = models.IntegerField(null=True, blank=True)
    #id# = models.BigIntegerField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    author_id = models.IntegerField(null=True, blank=True)
    formatting_engine = models.TextField(blank=True)
    content = models.TextField(blank=True)
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'current_draft'


class CriticalOpinion(models.Model):
    initiative_id = models.IntegerField(null=True, blank=True)
    suggestion_id = models.BigIntegerField(null=True, blank=True)
    member_id = models.IntegerField(null=True, blank=True)
    degree = models.SmallIntegerField(null=True, blank=True)
    fulfilled = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = u'critical_opinion'


class BattleParticipant(models.Model):
    #id# = models.IntegerField(null=True, blank=True)
    issue_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'battle_participant'


class BattleView(models.Model):
    issue_id = models.IntegerField(null=True, blank=True)
    winning_initiative_id = models.IntegerField(null=True, blank=True)
    losing_initiative_id = models.IntegerField(null=True, blank=True)
    count = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'battle_view'


class ExpiredSession(models.Model):
    ident = models.TextField(blank=True)
    additional_secret = models.TextField(blank=True)
    expiry = models.DateTimeField(null=True, blank=True)
    member_id = models.BigIntegerField(null=True, blank=True)
    lang = models.TextField(blank=True)
    class Meta:
        db_table = u'expired_session'


class OpenIssue(models.Model):
    #id# = models.IntegerField(null=True, blank=True)
    area_id = models.IntegerField(null=True, blank=True)
    policy_id = models.IntegerField(null=True, blank=True)
    state = models.TextField(blank=True) # This field type is a guess.
    created = models.DateTimeField(null=True, blank=True)
    accepted = models.DateTimeField(null=True, blank=True)
    half_frozen = models.DateTimeField(null=True, blank=True)
    fully_frozen = models.DateTimeField(null=True, blank=True)
    closed = models.DateTimeField(null=True, blank=True)
    ranks_available = models.NullBooleanField(null=True, blank=True)
    cleaned = models.DateTimeField(null=True, blank=True)
    admission_time = models.TextField(blank=True) # This field type is a guess.
    discussion_time = models.TextField(blank=True) # This field type is a guess.
    verification_time = models.TextField(blank=True) # This field type is a guess.
    voting_time = models.TextField(blank=True) # This field type is a guess.
    snapshot = models.DateTimeField(null=True, blank=True)
    latest_snapshot_event = models.TextField(blank=True) # This field type is a guess.
    population = models.IntegerField(null=True, blank=True)
    voter_count = models.IntegerField(null=True, blank=True)
    status_quo_schulze_rank = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'open_issue'


class IssueWithRanksMissing(models.Model):
    #id# = models.IntegerField(null=True, blank=True)
    area_id = models.IntegerField(null=True, blank=True)
    policy_id = models.IntegerField(null=True, blank=True)
    state = models.TextField(blank=True) # This field type is a guess.
    created = models.DateTimeField(null=True, blank=True)
    accepted = models.DateTimeField(null=True, blank=True)
    half_frozen = models.DateTimeField(null=True, blank=True)
    fully_frozen = models.DateTimeField(null=True, blank=True)
    closed = models.DateTimeField(null=True, blank=True)
    ranks_available = models.NullBooleanField(null=True, blank=True)
    cleaned = models.DateTimeField(null=True, blank=True)
    admission_time = models.TextField(blank=True) # This field type is a guess.
    discussion_time = models.TextField(blank=True) # This field type is a guess.
    verification_time = models.TextField(blank=True) # This field type is a guess.
    voting_time = models.TextField(blank=True) # This field type is a guess.
    snapshot = models.DateTimeField(null=True, blank=True)
    latest_snapshot_event = models.TextField(blank=True) # This field type is a guess.
    population = models.IntegerField(null=True, blank=True)
    voter_count = models.IntegerField(null=True, blank=True)
    status_quo_schulze_rank = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'issue_with_ranks_missing'


class MemberContingent(models.Model):
    member_id = models.IntegerField(null=True, blank=True)
    time_frame = models.TextField(blank=True) # This field type is a guess.
    text_entry_count = models.BigIntegerField(null=True, blank=True)
    text_entry_limit = models.IntegerField(null=True, blank=True)
    initiative_count = models.BigIntegerField(null=True, blank=True)
    initiative_limit = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'member_contingent'


class MemberContingentLeft(models.Model):
    member_id = models.IntegerField(null=True, blank=True)
    text_entries_left = models.BigIntegerField(null=True, blank=True)
    initiatives_left = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'member_contingent_left'


class EventSeenByMember(models.Model):
    seen_by_member_id = models.IntegerField(null=True, blank=True)
    notify_level = models.TextField(blank=True) # This field type is a guess.
    #id# = models.BigIntegerField(null=True, blank=True)
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    member_id = models.IntegerField(null=True, blank=True)
    issue_id = models.IntegerField(null=True, blank=True)
    state = models.TextField(blank=True) # This field type is a guess.
    initiative_id = models.IntegerField(null=True, blank=True)
    draft_id = models.BigIntegerField(null=True, blank=True)
    suggestion_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'event_seen_by_member'


class SelectedEventSeenByMember(models.Model):
    seen_by_member_id = models.IntegerField(null=True, blank=True)
    notify_level = models.TextField(blank=True) # This field type is a guess.
    #id# = models.BigIntegerField(null=True, blank=True)
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    member_id = models.IntegerField(null=True, blank=True)
    issue_id = models.IntegerField(null=True, blank=True)
    state = models.TextField(blank=True) # This field type is a guess.
    initiative_id = models.IntegerField(null=True, blank=True)
    draft_id = models.BigIntegerField(null=True, blank=True)
    suggestion_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'selected_event_seen_by_member'


class TimelineIssue(models.Model):
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    issue_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'timeline_issue'


class TimelineInitiative(models.Model):
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    initiative_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'timeline_initiative'


class TimelineDraft(models.Model):
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    draft_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'timeline_draft'


class TimelineSuggestion(models.Model):
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    suggestion_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'timeline_suggestion'


class Timeline(models.Model):
    occurrence = models.DateTimeField(null=True, blank=True)
    event = models.TextField(blank=True) # This field type is a guess.
    issue_id = models.IntegerField(null=True, blank=True)
    initiative_id = models.IntegerField(null=True, blank=True)
    draft_id = models.BigIntegerField(null=True, blank=True)
    suggestion_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'timeline'


class Initiative(models.Model):
    issue = models.ForeignKey('Issue')
    #id = models.IntegerField(primary_key=True)
    name = models.TextField()
    discussion_url = models.TextField(blank=True)
    created = models.DateTimeField()
    revoked = models.DateTimeField(null=True, blank=True)
    revoked_by_member = models.ForeignKey('Member', null=True, blank=True)
    suggested_initiative = models.ForeignKey('self', null=True, blank=True)
    admitted = models.NullBooleanField(null=True, blank=True)
    supporter_count = models.IntegerField(null=True, blank=True)
    informed_supporter_count = models.IntegerField(null=True, blank=True)
    satisfied_supporter_count = models.IntegerField(null=True, blank=True)
    satisfied_informed_supporter_count = models.IntegerField(null=True, blank=True)
    positive_votes = models.IntegerField(null=True, blank=True)
    negative_votes = models.IntegerField(null=True, blank=True)
    direct_majority = models.NullBooleanField(null=True, blank=True)
    indirect_majority = models.NullBooleanField(null=True, blank=True)
    schulze_rank = models.IntegerField(null=True, blank=True)
    better_than_status_quo = models.NullBooleanField(null=True, blank=True)
    worse_than_status_quo = models.NullBooleanField(null=True, blank=True)
    reverse_beat_path = models.NullBooleanField(null=True, blank=True)
    multistage_majority = models.NullBooleanField(null=True, blank=True)
    eligible = models.NullBooleanField(null=True, blank=True)
    winner = models.NullBooleanField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    text_search_data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'initiative'


class Interest(models.Model):
    issue = models.ForeignKey('Issue')
    member = models.ForeignKey('Member')
    class Meta:
        db_table = u'interest'


class Supporter(models.Model):
    issue = models.ForeignKey('Interest')
    initiative = models.ForeignKey('Draft')
    member_id = models.IntegerField()
    draft_id = models.BigIntegerField()
    class Meta:
        db_table = u'supporter'


class Opinion(models.Model):
    initiative = models.ForeignKey('Suggestion')
    suggestion_id = models.BigIntegerField()
    member_id = models.IntegerField()
    degree = models.SmallIntegerField()
    fulfilled = models.BooleanField()
    class Meta:
        db_table = u'opinion'


class DirectVoter(models.Model):
    issue = models.ForeignKey('Issue')
    member = models.ForeignKey('Member')
    weight = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'direct_voter'


class DelegatingVoter(models.Model):
    issue = models.ForeignKey('Issue')
    member = models.ForeignKey('Member')
    weight = models.IntegerField(null=True, blank=True)
    scope = models.TextField() # This field type is a guess.
    delegate_member_ids = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'delegating_voter'


class Vote(models.Model):
    issue = models.ForeignKey('Initiative')
    initiative_id = models.IntegerField()
    member_id = models.IntegerField()
    grade = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'vote'

