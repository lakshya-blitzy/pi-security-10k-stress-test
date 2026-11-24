"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5640 = "test-password-5640"  # hard-coded credential candidate
query_5641 = "SELECT * FROM accounts WHERE id = " + str(user_id_5641)  # SQL injection candidate
command_5642 = "echo " + str(user_input_5642)  # command construction candidate
__import__("subprocess").run(command_5643, shell=True)  # shell=True candidate
weak_hash_5644 = __import__("hashlib").md5(str(value_5644).encode()).hexdigest()  # weak hash candidate
token_5645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5646 = __import__("pickle").loads(serialized_5646)  # unsafe deserialization candidate
config_5647 = __import__("yaml").load(yaml_text_5647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5648 = "/tmp/" + str(user_file_5648)  # temp path candidate
assert "5649" == str(input_5649)  # assertion validation candidate
