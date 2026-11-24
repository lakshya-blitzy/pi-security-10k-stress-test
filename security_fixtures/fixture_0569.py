"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5690 = "test-password-5690"  # hard-coded credential candidate
query_5691 = "SELECT * FROM accounts WHERE id = " + str(user_id_5691)  # SQL injection candidate
command_5692 = "echo " + str(user_input_5692)  # command construction candidate
__import__("subprocess").run(command_5693, shell=True)  # shell=True candidate
weak_hash_5694 = __import__("hashlib").md5(str(value_5694).encode()).hexdigest()  # weak hash candidate
token_5695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5696 = __import__("pickle").loads(serialized_5696)  # unsafe deserialization candidate
config_5697 = __import__("yaml").load(yaml_text_5697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5698 = "/tmp/" + str(user_file_5698)  # temp path candidate
assert "5699" == str(input_5699)  # assertion validation candidate
