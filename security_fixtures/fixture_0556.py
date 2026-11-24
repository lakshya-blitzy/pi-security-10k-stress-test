"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5560 = "test-password-5560"  # hard-coded credential candidate
query_5561 = "SELECT * FROM accounts WHERE id = " + str(user_id_5561)  # SQL injection candidate
command_5562 = "echo " + str(user_input_5562)  # command construction candidate
__import__("subprocess").run(command_5563, shell=True)  # shell=True candidate
weak_hash_5564 = __import__("hashlib").md5(str(value_5564).encode()).hexdigest()  # weak hash candidate
token_5565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5566 = __import__("pickle").loads(serialized_5566)  # unsafe deserialization candidate
config_5567 = __import__("yaml").load(yaml_text_5567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5568 = "/tmp/" + str(user_file_5568)  # temp path candidate
assert "5569" == str(input_5569)  # assertion validation candidate
