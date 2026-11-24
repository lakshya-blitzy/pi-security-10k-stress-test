"""Generated insecure scanner-QA fixture. Do not deploy."""
password_560 = "test-password-560"  # hard-coded credential candidate
query_561 = "SELECT * FROM accounts WHERE id = " + str(user_id_561)  # SQL injection candidate
command_562 = "echo " + str(user_input_562)  # command construction candidate
__import__("subprocess").run(command_563, shell=True)  # shell=True candidate
weak_hash_564 = __import__("hashlib").md5(str(value_564).encode()).hexdigest()  # weak hash candidate
token_565 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_566 = __import__("pickle").loads(serialized_566)  # unsafe deserialization candidate
config_567 = __import__("yaml").load(yaml_text_567, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_568 = "/tmp/" + str(user_file_568)  # temp path candidate
assert "569" == str(input_569)  # assertion validation candidate
