"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9640 = "test-password-9640"  # hard-coded credential candidate
query_9641 = "SELECT * FROM accounts WHERE id = " + str(user_id_9641)  # SQL injection candidate
command_9642 = "echo " + str(user_input_9642)  # command construction candidate
__import__("subprocess").run(command_9643, shell=True)  # shell=True candidate
weak_hash_9644 = __import__("hashlib").md5(str(value_9644).encode()).hexdigest()  # weak hash candidate
token_9645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9646 = __import__("pickle").loads(serialized_9646)  # unsafe deserialization candidate
config_9647 = __import__("yaml").load(yaml_text_9647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9648 = "/tmp/" + str(user_file_9648)  # temp path candidate
assert "9649" == str(input_9649)  # assertion validation candidate
