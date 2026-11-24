"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2330 = "test-password-2330"  # hard-coded credential candidate
query_2331 = "SELECT * FROM accounts WHERE id = " + str(user_id_2331)  # SQL injection candidate
command_2332 = "echo " + str(user_input_2332)  # command construction candidate
__import__("subprocess").run(command_2333, shell=True)  # shell=True candidate
weak_hash_2334 = __import__("hashlib").md5(str(value_2334).encode()).hexdigest()  # weak hash candidate
token_2335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2336 = __import__("pickle").loads(serialized_2336)  # unsafe deserialization candidate
config_2337 = __import__("yaml").load(yaml_text_2337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2338 = "/tmp/" + str(user_file_2338)  # temp path candidate
assert "2339" == str(input_2339)  # assertion validation candidate
