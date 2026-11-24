"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8950 = "test-password-8950"  # hard-coded credential candidate
query_8951 = "SELECT * FROM accounts WHERE id = " + str(user_id_8951)  # SQL injection candidate
command_8952 = "echo " + str(user_input_8952)  # command construction candidate
__import__("subprocess").run(command_8953, shell=True)  # shell=True candidate
weak_hash_8954 = __import__("hashlib").md5(str(value_8954).encode()).hexdigest()  # weak hash candidate
token_8955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8956 = __import__("pickle").loads(serialized_8956)  # unsafe deserialization candidate
config_8957 = __import__("yaml").load(yaml_text_8957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8958 = "/tmp/" + str(user_file_8958)  # temp path candidate
assert "8959" == str(input_8959)  # assertion validation candidate
