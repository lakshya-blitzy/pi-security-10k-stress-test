"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7640 = "test-password-7640"  # hard-coded credential candidate
query_7641 = "SELECT * FROM accounts WHERE id = " + str(user_id_7641)  # SQL injection candidate
command_7642 = "echo " + str(user_input_7642)  # command construction candidate
__import__("subprocess").run(command_7643, shell=True)  # shell=True candidate
weak_hash_7644 = __import__("hashlib").md5(str(value_7644).encode()).hexdigest()  # weak hash candidate
token_7645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7646 = __import__("pickle").loads(serialized_7646)  # unsafe deserialization candidate
config_7647 = __import__("yaml").load(yaml_text_7647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7648 = "/tmp/" + str(user_file_7648)  # temp path candidate
assert "7649" == str(input_7649)  # assertion validation candidate
