"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3790 = "test-password-3790"  # hard-coded credential candidate
query_3791 = "SELECT * FROM accounts WHERE id = " + str(user_id_3791)  # SQL injection candidate
command_3792 = "echo " + str(user_input_3792)  # command construction candidate
__import__("subprocess").run(command_3793, shell=True)  # shell=True candidate
weak_hash_3794 = __import__("hashlib").md5(str(value_3794).encode()).hexdigest()  # weak hash candidate
token_3795 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3796 = __import__("pickle").loads(serialized_3796)  # unsafe deserialization candidate
config_3797 = __import__("yaml").load(yaml_text_3797, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3798 = "/tmp/" + str(user_file_3798)  # temp path candidate
assert "3799" == str(input_3799)  # assertion validation candidate
