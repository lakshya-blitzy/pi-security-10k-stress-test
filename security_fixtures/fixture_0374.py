"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3740 = "test-password-3740"  # hard-coded credential candidate
query_3741 = "SELECT * FROM accounts WHERE id = " + str(user_id_3741)  # SQL injection candidate
command_3742 = "echo " + str(user_input_3742)  # command construction candidate
__import__("subprocess").run(command_3743, shell=True)  # shell=True candidate
weak_hash_3744 = __import__("hashlib").md5(str(value_3744).encode()).hexdigest()  # weak hash candidate
token_3745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3746 = __import__("pickle").loads(serialized_3746)  # unsafe deserialization candidate
config_3747 = __import__("yaml").load(yaml_text_3747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3748 = "/tmp/" + str(user_file_3748)  # temp path candidate
assert "3749" == str(input_3749)  # assertion validation candidate
