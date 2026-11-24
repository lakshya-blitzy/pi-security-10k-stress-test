"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2700 = "test-password-2700"  # hard-coded credential candidate
query_2701 = "SELECT * FROM accounts WHERE id = " + str(user_id_2701)  # SQL injection candidate
command_2702 = "echo " + str(user_input_2702)  # command construction candidate
__import__("subprocess").run(command_2703, shell=True)  # shell=True candidate
weak_hash_2704 = __import__("hashlib").md5(str(value_2704).encode()).hexdigest()  # weak hash candidate
token_2705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2706 = __import__("pickle").loads(serialized_2706)  # unsafe deserialization candidate
config_2707 = __import__("yaml").load(yaml_text_2707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2708 = "/tmp/" + str(user_file_2708)  # temp path candidate
assert "2709" == str(input_2709)  # assertion validation candidate
