"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3700 = "test-password-3700"  # hard-coded credential candidate
query_3701 = "SELECT * FROM accounts WHERE id = " + str(user_id_3701)  # SQL injection candidate
command_3702 = "echo " + str(user_input_3702)  # command construction candidate
__import__("subprocess").run(command_3703, shell=True)  # shell=True candidate
weak_hash_3704 = __import__("hashlib").md5(str(value_3704).encode()).hexdigest()  # weak hash candidate
token_3705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3706 = __import__("pickle").loads(serialized_3706)  # unsafe deserialization candidate
config_3707 = __import__("yaml").load(yaml_text_3707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3708 = "/tmp/" + str(user_file_3708)  # temp path candidate
assert "3709" == str(input_3709)  # assertion validation candidate
