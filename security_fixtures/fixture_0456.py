"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4560 = "test-password-4560"  # hard-coded credential candidate
query_4561 = "SELECT * FROM accounts WHERE id = " + str(user_id_4561)  # SQL injection candidate
command_4562 = "echo " + str(user_input_4562)  # command construction candidate
__import__("subprocess").run(command_4563, shell=True)  # shell=True candidate
weak_hash_4564 = __import__("hashlib").md5(str(value_4564).encode()).hexdigest()  # weak hash candidate
token_4565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4566 = __import__("pickle").loads(serialized_4566)  # unsafe deserialization candidate
config_4567 = __import__("yaml").load(yaml_text_4567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4568 = "/tmp/" + str(user_file_4568)  # temp path candidate
assert "4569" == str(input_4569)  # assertion validation candidate
