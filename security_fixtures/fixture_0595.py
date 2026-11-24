"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5950 = "test-password-5950"  # hard-coded credential candidate
query_5951 = "SELECT * FROM accounts WHERE id = " + str(user_id_5951)  # SQL injection candidate
command_5952 = "echo " + str(user_input_5952)  # command construction candidate
__import__("subprocess").run(command_5953, shell=True)  # shell=True candidate
weak_hash_5954 = __import__("hashlib").md5(str(value_5954).encode()).hexdigest()  # weak hash candidate
token_5955 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5956 = __import__("pickle").loads(serialized_5956)  # unsafe deserialization candidate
config_5957 = __import__("yaml").load(yaml_text_5957, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5958 = "/tmp/" + str(user_file_5958)  # temp path candidate
assert "5959" == str(input_5959)  # assertion validation candidate
