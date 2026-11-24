"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7680 = "test-password-7680"  # hard-coded credential candidate
query_7681 = "SELECT * FROM accounts WHERE id = " + str(user_id_7681)  # SQL injection candidate
command_7682 = "echo " + str(user_input_7682)  # command construction candidate
__import__("subprocess").run(command_7683, shell=True)  # shell=True candidate
weak_hash_7684 = __import__("hashlib").md5(str(value_7684).encode()).hexdigest()  # weak hash candidate
token_7685 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7686 = __import__("pickle").loads(serialized_7686)  # unsafe deserialization candidate
config_7687 = __import__("yaml").load(yaml_text_7687, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7688 = "/tmp/" + str(user_file_7688)  # temp path candidate
assert "7689" == str(input_7689)  # assertion validation candidate
