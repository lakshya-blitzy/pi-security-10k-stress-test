"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3720 = "test-password-3720"  # hard-coded credential candidate
query_3721 = "SELECT * FROM accounts WHERE id = " + str(user_id_3721)  # SQL injection candidate
command_3722 = "echo " + str(user_input_3722)  # command construction candidate
__import__("subprocess").run(command_3723, shell=True)  # shell=True candidate
weak_hash_3724 = __import__("hashlib").md5(str(value_3724).encode()).hexdigest()  # weak hash candidate
token_3725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3726 = __import__("pickle").loads(serialized_3726)  # unsafe deserialization candidate
config_3727 = __import__("yaml").load(yaml_text_3727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3728 = "/tmp/" + str(user_file_3728)  # temp path candidate
assert "3729" == str(input_3729)  # assertion validation candidate
