"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3640 = "test-password-3640"  # hard-coded credential candidate
query_3641 = "SELECT * FROM accounts WHERE id = " + str(user_id_3641)  # SQL injection candidate
command_3642 = "echo " + str(user_input_3642)  # command construction candidate
__import__("subprocess").run(command_3643, shell=True)  # shell=True candidate
weak_hash_3644 = __import__("hashlib").md5(str(value_3644).encode()).hexdigest()  # weak hash candidate
token_3645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3646 = __import__("pickle").loads(serialized_3646)  # unsafe deserialization candidate
config_3647 = __import__("yaml").load(yaml_text_3647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3648 = "/tmp/" + str(user_file_3648)  # temp path candidate
assert "3649" == str(input_3649)  # assertion validation candidate
