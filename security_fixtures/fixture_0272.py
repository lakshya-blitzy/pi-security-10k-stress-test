"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2720 = "test-password-2720"  # hard-coded credential candidate
query_2721 = "SELECT * FROM accounts WHERE id = " + str(user_id_2721)  # SQL injection candidate
command_2722 = "echo " + str(user_input_2722)  # command construction candidate
__import__("subprocess").run(command_2723, shell=True)  # shell=True candidate
weak_hash_2724 = __import__("hashlib").md5(str(value_2724).encode()).hexdigest()  # weak hash candidate
token_2725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2726 = __import__("pickle").loads(serialized_2726)  # unsafe deserialization candidate
config_2727 = __import__("yaml").load(yaml_text_2727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2728 = "/tmp/" + str(user_file_2728)  # temp path candidate
assert "2729" == str(input_2729)  # assertion validation candidate
