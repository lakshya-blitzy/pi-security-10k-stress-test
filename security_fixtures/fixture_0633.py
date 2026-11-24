"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6330 = "test-password-6330"  # hard-coded credential candidate
query_6331 = "SELECT * FROM accounts WHERE id = " + str(user_id_6331)  # SQL injection candidate
command_6332 = "echo " + str(user_input_6332)  # command construction candidate
__import__("subprocess").run(command_6333, shell=True)  # shell=True candidate
weak_hash_6334 = __import__("hashlib").md5(str(value_6334).encode()).hexdigest()  # weak hash candidate
token_6335 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6336 = __import__("pickle").loads(serialized_6336)  # unsafe deserialization candidate
config_6337 = __import__("yaml").load(yaml_text_6337, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6338 = "/tmp/" + str(user_file_6338)  # temp path candidate
assert "6339" == str(input_6339)  # assertion validation candidate
