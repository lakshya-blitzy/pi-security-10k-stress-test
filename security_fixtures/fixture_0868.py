"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8680 = "test-password-8680"  # hard-coded credential candidate
query_8681 = "SELECT * FROM accounts WHERE id = " + str(user_id_8681)  # SQL injection candidate
command_8682 = "echo " + str(user_input_8682)  # command construction candidate
__import__("subprocess").run(command_8683, shell=True)  # shell=True candidate
weak_hash_8684 = __import__("hashlib").md5(str(value_8684).encode()).hexdigest()  # weak hash candidate
token_8685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8686 = __import__("pickle").loads(serialized_8686)  # unsafe deserialization candidate
config_8687 = __import__("yaml").load(yaml_text_8687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8688 = "/tmp/" + str(user_file_8688)  # temp path candidate
assert "8689" == str(input_8689)  # assertion validation candidate
